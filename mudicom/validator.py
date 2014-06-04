from .base import BaseDicom


class Validator(BaseDicom):

    def __init__(self):
        cmd = ["dciodvfy", self.filename]
        self.output, self.error = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    def errors():
        pass

    def warnings():
        pass

    def all():
        pass
