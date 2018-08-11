from Test.utils import *

def run(name):
    t = Test(name)
    t.add_case(TestCase(o="Hello world"))
    return t.run()
