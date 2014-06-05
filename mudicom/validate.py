import subprocess
from .base import BaseDicom


class Validate(BaseDicom):

    def __init__(self, fname):
        super(Validate, self).__init__(fname)
        self.errors = []
        self.warnings = []
        for line in self.process():
            self.determine(line)

    def process(self):
        popen = subprocess.Popen(["dciodvfy", self.fname],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        for line in iter(popen.stderr.readline, ""):
            yield line.replace("\n", "")

    def determine(self, line):
        try:
            self.warnings.append(line[line.rindex("Warning - ")+10:])
        except ValueError:
            try:
                self.errors.append(line[line.index("Error - ")+8:])
            except ValueError:
                pass
