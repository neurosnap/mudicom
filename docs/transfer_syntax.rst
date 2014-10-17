===============
Transfer Syntax
===============

    A transfer syntax is a set of encoding rules that allow Application
    Entities to unambiguously negotiate the encoding techniques
    (e.g., Data Element structure, byte ordering, compression) they are
    able to support, thereby allowing these Application Entities to
    communicate.

    -- `DICOM Standard 3.10`_

    .. _`DICOM Standard 3.10`: http://www.dabsoft.ch/dicom/5/3.10/

The Transfer Syntax UID is the unique identifier used as a tag in the DICOM
standard to determine the type of encoding principles used for any given
DICOM file. The Transfer Syntax UID is in the file DICOM Tag
field (0002,0010).

The following list are the currently supported transfer syntaxes
for mudicom:

+------------------------+----------------------------------------------+
|  Transfer Syntax UID   |               Description                    |
+========================+==============================================+
| 1.2.840.10008.1.2      | Implicit VR - Little Endian                  |
+------------------------+----------------------------------------------+
| 1.2.840.100 08.1.2.1   | Explicit VR - Little Endian                  |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.1.99 | Deflated Explicit VR - Little Endian         |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.2    | Explicit VR - Big Endian                     |
+------------------------+----------------------------------------------+
| 1.2.840.113619.5.2     | Implicit VR - Big Endian (G.E Private)       |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.5    | Run Length Encoding, Lossless                |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.4.50 | JPEG Baseline (Process 1)                    |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.4.51 | JPEG Extended (Process 2 & 4)                |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.4.57 | JPEG Lossless, Non-Hierarchical (Process 14) |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.4.70 | JPEG Lossless, Hierarchical,                 |
|                        | First-Order Prediction                       |
|                        | (Process 14, [sec. 1])                       |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.4.90 | JPEG 2000 Image Compression (Lossless Only)  |
+------------------------+----------------------------------------------+
| 1.2.840.10008.1.2.4.91 | JPEG 2000 Image Compression                  |
+------------------------+----------------------------------------------+

These are the unsupported transfer syntaxes:

+-------------------------+-------------------------------------------------------------+
|   Transfer Syntax UID   |                      Description                            |
+=========================+=============================================================+
| 1.2.840.10008.1.2.4.52  | JPEG Extended (Process 3 & 5)                               |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.53  | JPEG Spectral Selection, Non-Hierarchical (Process 6 & 8)   |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.54  | JPEG Spectral Selection, Non-Hierarchical (Proce  ss 7 & 9) |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.55  | JPEG Full Progression, Non-Hierarchical (Process 10 & 12)   |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.56  | JPEG Full Progression, Non-Hierarchical (Process 11 & 13)   |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.59  | JPEG Extended, Hierarchical (Process 16 & 18)               |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.60  | JPEG Extended, Hierarchical (Process 17 & 19)               |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.61  | JPEG Spectral Selection, Hierarchical (Process 20 & 22)     |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.62  | JPEG Spectral Selection, Hierarchical (Process 21 & 23)     |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.63  | JPEG Full Progression, Hierarchical (Process 24 & 26)       |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.64  | JPEG Full Progression, Hierarchical (Process 25 & 27)       |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.80  | (partial) JPEG-LS Lossless Image Compression                |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.81  | (partial) JPEG-LS Lossy (Near-Lossless) Image Compression   |
+-------------------------+-------------------------------------------------------------+
| 1.2.840.10008.1.2.4.100 | (partial) MPEG2 Main Profile @ Main Level                   |
+-------------------------+-------------------------------------------------------------+
