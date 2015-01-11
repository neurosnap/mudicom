# -*- coding: utf-8 -*-
"""
    mudicom.lookup
    ~~~~~~~~~~~~~~

    Basic dictionary lookup helper functions.
"""
def VR(VR=None, description=None):
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
    assert VR or description, "Either VR or description required to map VR"

    if VR is not None:
        VR = VR.upper()
        if VR in value_repr:
            return value_repr[VR]

    for key, value in value_repr.iteritems():
        if description == value:
            return key

    return None

def transfer_syntax(UID=None, description=None):
    """ Transfer Syntax UID <-> Description lookup.

    :param UID: Transfer Syntax UID, returns description
    :param description: Take the description of a transfer syntax and return its UID
    """
    transfer_syntax = {
        "1.2.840.10008.1.2": "Implicit VR Endian: Default Transfer Syntax for DICOM",
        "1.2.840.10008.1.2.1": "Explicit VR Little Endian",
        "1.2.840.10008.1.2.1.99": "Deflated Explicit VR Big Endian",
        "1.2.840.10008.1.2.2": "Explicit VR Big Endian",
        "1.2.840.10008.1.2.4.50": "JPEG Baseline (Process 1): Default Transfer Syntax for Lossy JPEG 8-bit Image Compression",
        "1.2.840.10008.1.2.4.51": "JPEG Baseline (Processes 2 & 4): Default Transfer Syntax for Lossy JPEG 12-bit Image Compression (Process 4 only)",
        "1.2.840.10008.1.2.4.57": "JPEG Lossless, Nonhierarchical (Processes 14)",
        "1.2.840.10008.1.2.4.70": "JPEG Lossless, Nonhierarchical, First-Order Prediction (Processes 14 [Selection Value 1])",
        "1.2.840.10008.1.2.4.80": "JPEG-LS Lossless Image Compression",
        "1.2.840.10008.1.2.4.81": "JPEG-LS Lossy (Near- Lossless) Image Compression",
        "1.2.840.10008.1.2.4.90": "JPEG 2000 Image Compression (Lossless Only)",
        "1.2.840.10008.1.2.4.91": "JPEG 2000 Image Compression",
        "1.2.840.10008.1.2.4.92": "JPEG 2000 Part 2 Multicomponent Image Compression (Lossless Only)",
        "1.2.840.10008.1.2.4.93": "JPEG 2000 Part 2 Multicomponent Image Compression",
        "1.2.840.10008.1.2.4.94": "JPIP Referenced",
        "1.2.840.10008.1.2.4.95": "JPIP Referenced Deflate",
        "1.2.840.10008.1.2.5": "RLE Lossless",
        "1.2.840.10008.1.2.6.1": "RFC 2557 MIME Encapsulation",
        "1.2.840.10008.1.2.4.100": "MPEG2 Main Profile Main Level",
        "1.2.840.10008.1.2.4.102": "MPEG-4 AVC/H.264 High Profile / Level 4.1",
        "1.2.840.10008.1.2.4.103": "MPEG-4 AVC/H.264 BD-compatible High Profile / Level 4.1"
    }
    assert UID or description, "Either Transfer syntax UID or description required"

    if UID in transfer_syntax:
        return transfer_syntax[UID]

    for key, value in transfer_syntax.iteritems():
        if description == value:
            return key

    return None
