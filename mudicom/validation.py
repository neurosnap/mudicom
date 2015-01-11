# -*- coding: utf-8 -*-
"""
    mudicom.validation
    ~~~~~~~~~~~~~~~~~~

    DICOM validation module that uses dicom3tools' command line utility,
    `dciodvfy`.
"""
import subprocess

def _process(fname):
    popen = subprocess.Popen(["dciodvfy", fname],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    for line in iter(popen.stderr.readline, ""):
        yield line.replace("\n", "")

def _determine(line):
    try:
        return "warnings", line[line.rindex("Warning - ") + 10:]
    except ValueError:
        try:
            return "errors", line[line.index("Error - ") + 8:]
        except ValueError:
            return None, None

def validate(fname):
    """ This function uses dciodvfy to generate
    a list of warnings and errors discovered within
    the DICOM file.

    :param fname: Location and filename of DICOM file.
    """
    validation = {
        "errors": [],
        "warnings": []
    }
    for line in _process(fname):
        kind, message = _determine(line)
        if kind in validation:
            validation[kind].append(message)
    return validation