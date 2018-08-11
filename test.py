import os
import importlib
from make import *

def test():
    for test in os.listdir(TEST_DIR):
        if test == "__pycache__" or test == "utils.py":
            continue
        name = test[:-3]
        print(bcolors.HEADER + "CHECK " + bcolors.ENDC, end='')
        print(test + "\t\t", end='')
        if not os.path.exists(BUILD_DIR + name):
            print(bcolors.FAIL + "FAIL: " + bcolors.ENDC, end='')
            print("File " + name + " not exists in " + BUILD_DIR)
            continue

        test_module = importlib.import_module('Test.' + name)
        result = test_module.run(BUILD_DIR + name)
        if result[0]:
            print(bcolors.OKGREEN + "Success" + bcolors.ENDC, end='')
        else:
            print(bcolors.FAIL + "Fail: " + bcolors.ENDC + "Test "
                  + str(result[1]) + " Expected: " + str(result[2]) + " Got: " + str(result[3]), end='')
        print()

if __name__ == "__main__":
    test()
