from subprocess import Popen, PIPE, STDOUT
class Test:
    def __init__(self, program):
        self.cases = list()
        self.program = program

    def run(self):
        for ind, c in enumerate(self.cases):
            res = self.run_case(c)
            if not res[0]:
                return [False, ind, res[1], res[2]]
        return [True]

    def add_case(self, c):
        self.cases.append(c)

    def run_case(self, c):
        p = Popen([self.program], stdout=PIPE, stdin=PIPE)
        out = p.communicate(input=c.input)[0].decode('ascii')

        if c.output.strip() != out.strip():
            return [False, str(c.output.strip()), out.strip()]
        return [True]

class TestCase:
    input = str()
    outout = str()
