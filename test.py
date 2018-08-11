import os
import importlib
from make import *

def test():
    for test in os.listdir(TEST_DIR):
        if test == "__pycache__":
            continue
        name = test[:-3]
        print(bcolors.HEADER + "CHECK " + bcolors.ENDC, end='')
        print(test + "\t\t", end='')
        if not os.path.exists(BUILD_DIR + name):
            print(bcolors.FAIL + "FAIL: " + bcolors.ENDC, end='')
            print("File " + name + " not exists in " + BUILD_DIR)
            continue

        test_module = importlib.import_module('Test.' + name)
        test_module.run()
        print()

if __name__ == "__main__":
    test()
