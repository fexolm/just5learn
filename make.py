import os

CUR_DIR = os.getcwd()
SOURCE_DIR=CUR_DIR + "/src/"
BUILD_DIR=CUR_DIR + "/build/"
CFLAGS="-O0 -g -Wall"
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
    ]
}


def build(program, files):
    cur_files = [SOURCE_DIR + f for f in files]
    cmd = "{} {} {} -o {}".format(COMPILER, CFLAGS, " ".join(cur_files), BUILD_DIR + program)
    os.system(cmd)
    print(cmd)


if not os.path.exists(BUILD_DIR):
    os.makedirs(BUILD_DIR)

for k, v in PROGRAMS.items():
    build(k, v)


