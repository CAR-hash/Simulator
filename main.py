# This is a sample Python script.
import collections

import numpy.random
# Press Shift+F10 to execute it or replace it with youSWr code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import simpy
import numpy as np
import requests
import json
import matplotlib.pyplot as plt

class PkgLRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.queue = collections.OrderedDict()

    # if pkg hit the cache, return true
    # else return false
    # update cache after that
    def update(self, pkg):
        if pkg[0] == -1:
            return True
        if pkg[1] > self.capacity:
            return False
        if pkg[0] not in self.queue:
            self.size = self.size + pkg[1]
            if self.size <= self.capacity:
                self.queue[pkg[0]] = pkg
            else:
                while self.size > self.capacity:
                    v = self.queue.popitem(last=False)
                    if type(v[1]) != float:
                        v = v[1]
                    self.size -= v[1]
                self.queue[pkg[0]] = pkg
            return False
        else:
            v = self.queue.pop(pkg[0])
            self.queue[pkg[0]] = v
            return True


class PackageSampler(object):
    def __init__(self):
        self.pool = [0.135, 0.124,11.3,0.0626,0.808,0.0316,0.0482,0.158,0.0798,0.0648,0.053,0.138,0.0615,0.247,2.5,0.0144,0.0111,15.7,2.1,0.121]

    def sample(self):
        rank = np.random.default_rng().zipf(1.1)
        size = max(np.random.default_rng().normal(loc=0.16, scale=1), 0.001)
        if rank <= 20:
            size = self.pool[rank-1]
        return rank, size

class Request(object):
    def __init__(self, pkgs, execution):
        self.pkgs = pkgs
        self.execution = execution
        self.max_pkg = (-1, 0)
        for pkg in pkgs:
            if self.max_pkg[1] < pkg[1]:
                self.max_pkg = pkg


class RandomRequest(Request):
    def __init__(self, sampler):
        pkgs = []

        pkg_count = int(np.floor(np.random.default_rng().exponential(scale=3)))
        for i in range(0, pkg_count):
            pkg = sampler.sample()
            pkgs.append(pkg)

        execution = np.random.default_rng().exponential(scale=100)
        super().__init__(pkgs, execution)

class Statistician(object):
    def __init__(self, worker_count = 1000):
        self.global_hit_count = [
            [],[],[]
        ]
        for mode in range(0, 3):
            for i in range(0, worker_count):
                self.global_hit_count[mode].append(0)
        self.global_total_count = [
            [],[],[]
        ]
        for mode in range(0, 3):
            for i in range(0, worker_count):
                self.global_total_count[mode].append(0)

        #
        self.active_tasks = [0, 0, 0]

    def show(self):
        hit = [[], [], []]
        for mode in range(0, 3):
            for i in range(0, 1000):
                if self.global_total_count[mode][i] == 0:
                    hit[mode].append(50)
                else:
                    hit[mode].append(
                        100 * self.global_hit_count[mode][i] / self.global_total_count[mode][i])

        labels = ["Least loaded", "Hash Affinity", "PASch"]
        fig, axs = plt.subplots()
        for i in range(0, 1000):
            # rectangular box plot
            bplot = axs.boxplot(hit,
                                vert=True,  # vertical box alignment
                                patch_artist=True,  # fill with color
                                labels=labels)  # will be used to label x-ticks
            axs.set_xlabel("Scheduling Algorithm")
            axs.set_ylabel("Hit rate(%)")
        plt.show()

class Worker(object):
    def __init__(self, sta: Statistician, mode, env: simpy.Environment, w_id: int, assign_task: simpy.Event):
        self.w_id = w_id
        self.env = env
        self.workload = []
        self.action = self.env.process(self.run())
        self.assign_task = assign_task
        self.st = 100
        self.cache = PkgLRUCache(capacity=500)
        self.sta = sta
        self.mode = mode
        self.local_hit_count = 0
        self.local_total_count = 0

    def run(self):
        while True:
            if len(self.workload) > 0:
                task = self.workload.pop(0)
                #hit = 0
                #total = len(task.pkgs)
                #for pkg in task.pkgs:
                #    if self.cache.update(pkg):
                #        hit = hit + 1
                self.sta.global_total_count[self.mode][self.w_id] = self.sta.global_total_count[self.mode][
                                                                        self.w_id] + 1
                if self.cache.update(task.max_pkg):
                    self.sta.global_hit_count[self.mode][self.w_id] = self.sta.global_hit_count[self.mode][self.w_id] + 1
                    turn_around = 1000 + task.execution
                else:
                    turn_around = np.random.default_rng().exponential(scale=4007) + 1000 + task.execution

                yield self.env.timeout(turn_around)
                self.sta.active_tasks[self.mode] = max(0, self.sta.active_tasks[self.mode]-1)
            else:
                yield self.assign_task

class Cloud(object):
    def __init__(self, env, sta, worker_count, mode="Least loaded"):
        self.env: simpy.Environment = env
        self.assign_task = []

        self.sta = sta

        self.mode = mode
        self.c = 1.25

        for i in range(worker_count):
            self.assign_task.append(self.env.event())
        self.workers = []

        self.n_mode = 0
        if mode == "Hash Affinity":
            self.n_mode = 1
        elif mode == "PASch":
            self.n_mode = 2
        for i in range(worker_count):
            self.workers.append(Worker(sta=self.sta, mode=self.n_mode, env=env, w_id=i, assign_task=self.assign_task[i]))

    def handle_request(self, req: Request):
        self.sta.active_tasks[self.n_mode] = self.sta.active_tasks[self.n_mode] + 1

        if self.mode == "Least loaded":
            w_id = 0
            for worker in self.workers:
                if len(worker.workload) < len(self.workers[w_id].workload):
                    w_id = worker.w_id
            self.__distribute_task_to(w_id, req)
        elif self.mode == "Hash Affinity":
            w_id = self.__m(req.max_pkg[0])
            self.__distribute_task_to(w_id, req)
        elif self.mode == "PASch":
            w_1 = self.__m(req.max_pkg[0])
            w_2 = self.__m(req.max_pkg[0] + 10)
            w_id = w_1
            if len(self.workers[w_2].workload) < len(self.workers[w_1].workload):
                w_id = w_2
            if len(self.workers[w_id].workload) > self.workers[w_id].st:
                for worker in self.workers:
                    if len(worker.workload) < len(self.workers[w_id].workload):
                        w_id = worker.w_id
            self.__distribute_task_to(w_id, req)

    def __m(self, pkg_id):
        return pkg_id % 1000
        idx = pkg_id % 1000
        first_search = True
        while True:
            if len(self.workers[idx].workload) < self.sta.active_tasks[self.n_mode]/800:
                break
            else:
                idx = idx + 1
                if idx >= 1000:
                    idx = 0
                    if first_search:
                        first_search = False
                    else:
                        idx = np.random.default_rng().choice(self.workers).w_id
                        break
        return idx

    def __distribute_task_to(self, worker_id, req):
        self.assign_task[worker_id].succeed()
        self.assign_task[worker_id] = self.env.event()
        self.workers[worker_id].workload.append(req)
        self.workers[worker_id].assign_task = self.assign_task[worker_id]


class RequestGenerator(object):
    def __init__(self, sta,env: simpy.Environment, cloud: list[Cloud], period):
        self.env = env
        self.sta = sta
        self.cloud = cloud
        self.period = period
        self.action = self.env.process(self.request_generator())
        self.env.process(self.timer())
        self.sampler = PackageSampler()

    def timer(self):
        yield self.env.timeout(self.period)
        self.action.interrupt()

    def request_generator(self):
        while True:
            try:
                yield self.env.timeout(np.random.default_rng().exponential(scale=0.1))
                self.cloud[1].handle_request(RandomRequest(sampler=self.sampler))
                for c in self.cloud:
                    c.handle_request(RandomRequest(sampler=self.sampler))
            except simpy.Interrupt:
                self.sta.show()
                print("now:{}, time to sleep...".format(self.env.now))
                break


def print_hi(name):
    env = simpy.Environment()

    statistician = Statistician()

    cloud = Cloud(env=env, sta=statistician, worker_count=1000,mode="Least loaded")
    cloud2 = Cloud(env=env, sta=statistician, worker_count=1000,mode="Hash Affinity")
    cloud3 = Cloud(env=env, sta=statistician, worker_count=1000,mode="PASch")
    generator = RequestGenerator(env=env, sta=statistician, cloud=[cloud, cloud2, cloud3], period=500)

    env.run()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #sampler = PackageSampler()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
