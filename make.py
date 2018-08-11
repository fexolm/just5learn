import os

CUR_DIR = os.getcwd()
SOURCE_DIR=CUR_DIR + "/src/"
BUILD_DIR=CUR_DIR + "/build/"
TEST_DIR=CUR_DIR + "/Test/"
CFLAGS="-O0 -g"
COMPILER="gcc"
PROGRAMS = {
    "find_number1" : [
        "find_number1.c"
    ],
    "find_number2" : [
        "find_number2.c"
    ],
    "say_hello" : [
        "say_hello.c"
    ],
    "reverse_array" : [
        "reverse_array.c",
        "utility.c",
        "utility.h"
    ],
    "vector" : [
        "vector.h",
        "vector.c",
        "vector_main.c"
    ],
    "permute_array" : [
        "permute_array.c",
        "utility.c",
        "utility.h"
    ],
    "euclidean_norm" : [
        "euclidean_norm.c"
    ]
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def build(program, files):
    cur_files = [SOURCE_DIR + f for f in files]
    cmd = "{} {} {} -o {}".format(COMPILER, CFLAGS, " ".join(cur_files), BUILD_DIR + program)
    os.system(cmd)
    print(cmd)

if __name__ == "__main__":
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)

    for k, v in PROGRAMS.items():
        build(k, v)



