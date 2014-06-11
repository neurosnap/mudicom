import os
import subprocess
from .base import BaseDicom


class Validate(BaseDicom):
    """ This class uses dciodvfy to generate 
    a list of warnings and errors discovered within
    the DICOM file.

    :param fname: Location and filename of DICOM file.
    """
    def __init__(self, fname):
        super(Validate, self).__init__(fname)
        self._errors = []
        self._warnings = []
        for line in self._process():
            self._determine(line)

    def _process(self):
        popen = subprocess.Popen(["dciodvfy", self.fname],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        for line in iter(popen.stderr.readline, ""):
            yield line.replace("\n", "")

    def _determine(self, line):
        try:
            self.warnings.append(line[line.rindex("Warning - ")+10:])
        except ValueError:
            try:
                self.errors.append(line[line.index("Error - ")+8:])
            except ValueError:
                pass

    def get_errors(self):
        """ Returns a list of errors 
        within the DICOM file
        """
        return self._errors

    def get_warnings(self):
        """ Returns a list of warnings
        within the DICOM file
        """
        return self._warnings