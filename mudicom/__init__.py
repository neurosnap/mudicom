import subprocess

from .base import BaseDicom

def load(fname):
    """ Imports DICOM file into memory, returns a DICOM session class

    :param fname: Location and filename of DICOM file.
    """
    return BaseDicom(fname)

def validate(fname):
    """ This function uses dciodvfy to generate 
    a list of warnings and errors discovered within
    the DICOM file.

    :param fname: Location and filename of DICOM file.
    """
    def _process():
        popen = subprocess.Popen(["dciodvfy", fname],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        for line in iter(popen.stderr.readline, ""):
            yield line.replace("\n", "")

    def _determine(line):
        try:
            return "warnings", line[line.rindex("Warning - ")+10:]
        except ValueError:
            try:
                return "errors", line[line.index("Error - ")+8:]
            except ValueError:
                return None, None

    validation = { 
        "errors": [], 
        "warnings": [] 
    }

    for line in _process():
        kind, message = _determine(line)
        if kind in validation:
            validation[kind].append(message)
    return validation

def lookup_VR(VR=None, description=None):
    """ Value Representation (VR) <-> Description lookup.

    :param VR: Takes the VR and returns its description
    :param description: Take the description of a VR and returns the VR
    """
    value_repr = {
        "AE": "Application Entity",
        "AS": "Age String",
        "AT": "Attribute Tag",
        "CS": "Code String",
        "DA": "Date",
        "DS": "Decimal String",
        "DT": "Date/Time",
        "FL": "Floating Point Single (4 bytes)",
        "FD": "Floating Point Double (8 bytes)",
        "IS": "Integer String",
        "LO": "Long String",
        "LT": "Long Text",
        "OB": "Other Byte",
        "OF": "Other Float",
        "OW": "Other Word",
        "PN": "Person Name",
        "SH": "Short String",
        "SL": "Signed Long",
        "SQ": "Sequence of Items",
        "SS": "Signed Short",
        "ST": "Short Text",
        "TM": "Time",
        "UI": "Unique Identifier",
        "UL": "Unsigned Long",
        "UN": "Unknown",
        "US": "Unsigned Short",
        "UT": "Unlimited Text"
    }
    if VR:
        if VR in value_repr:
            return value_repr[VR]
        else:
            raise Exception("VR not found in map")
    elif description:
        for key, value in value_repr.iteritems():
            if description == value:
                return key
        raise Exception("Description not found in map")
    else:
        raise Exception("Either VR or description required to map_VR")