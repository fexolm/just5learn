from Test.utils import *

def run(name):
    t = Test(name)
    case1 = TestCase()
    case1.output = "Hello world"
    t.add_case(case1)
    return t.run()
