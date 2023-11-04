# This is a sample Python script.
import math
import os
import random
import copy
# Press Shift+F10 to execute it or replace it with youSWr code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import numpy.random

def generate_handler(handler_name, pkgs):
    handler_path = 'handlers/%s' % handler_name
    os.makedirs(handler_path)
    imp_pkgs = copy.deepcopy(pkgs)
    for i in range(0, len(imp_pkgs)):
        if imp_pkgs[i] == 'typing-extensions':
            imp_pkgs[i] = 'typing_extensions'
        elif imp_pkgs[i] == 'charset-normalizer':
            imp_pkgs[i] = 'charset_normalizer'
        elif imp_pkgs[i] == 'python-dateutil':
            imp_pkgs[i] = 'dateutil'
        elif imp_pkgs[i] == 'pyasn1-modules':
            imp_pkgs[i] = 'pyasn1_modules'
        elif imp_pkgs[i] == 'google-auth-oauthlib':
            imp_pkgs[i] = 'google_auth_oauthlib'
        elif imp_pkgs[i] == 'pyyaml':
            imp_pkgs[i] = 'yaml'
    with open('%s/f.py' % handler_path, 'w') as f:
        imps = '\n'.join('import %s' % imp for imp in sorted(imp_pkgs))
        f.write(imps)
        handler = '''
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        '''
        f.write(handler)
    # write requirements
    with open('%s/requirements.in' % handler_path, 'w') as f:
        for pkg in pkgs:
            f.write(pkg + "\n")
def generate_handlers(req_path, handler_count):
    f = open(req_path, "r")
    pkgs = f.readlines()
    for i in range(0, len(pkgs)):
        pkgs[i] = pkgs[i].replace("\n", "")
    for i in range(0, handler_count):
        handler_name = 'hdl_%d' % i
        pkg_count = min(math.ceil(np.random.default_rng().exponential(scale=3)), 10)
        pkg_list = random.sample(pkgs, pkg_count)
        print(pkg_list)
        generate_handler(handler_name, pkg_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_handlers(req_path="requirements.txt", handler_count=100)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
