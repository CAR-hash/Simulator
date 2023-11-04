import requests
import time
import threading


def generate_requests(hdl_count):
    turn_around_time = []
    for i in range(0, hdl_count):
        t0 = time.time()
        requests.post(url="http://localhost:9020/runLambda/hdl_%d" % i, json='{"hello":"world"}')
        t1 = time.time()
        turn_around_time.append(t1 - t0)
    print(turn_around_time)


def single_shot(hdl_idx):
    turn_around_time = []
    t0 = time.time()
    requests.post(url="http://localhost:9020/runLambda/hdl_%d" % hdl_idx, json='{"hello":"world"}')
    t1 = time.time()
    turn_around_time.append(t1 - t0)
    print(turn_around_time)


turn_around_time_simul = {}


class RequestThread(threading.Thread):
    def __init__(self, thread_name, hdl_idx):
        super(RequestThread, self).__init__(name=thread_name)
        self.hdl_idx = hdl_idx

    def run(self) -> None:
        global turn_around_time_simul
        t0 = time.time()
        status = requests.post(url="http://localhost:9020/runLambda/hdl_%d" % self.hdl_idx,
                               json='{"hello":"world"}').status_code
        t1 = time.time()
        print("task %d finished with %d " % (self.hdl_idx, status))
        turn_around_time_simul[self.hdl_idx] = t1 - t0


def generate_requests_simultanously(hdl_count):
    trds = []
    for i in range(0, hdl_count):
        trd = RequestThread("%d" % i, i)
        trds.append(trd)
        print("task %d starts!" % i)
        trd.start()
        time.sleep(0.1)
    while True:
        all_dead = True
        for trd in trds:
            if trd.is_alive():
                all_dead = False
        if all_dead:
            break

    print(turn_around_time_simul)


if __name__ == '__main__':
    generate_requests_simultanously(hdl_count=100)
