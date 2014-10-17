========
Tutorial
========

The goal of mudicom is in a pythonic way interact with GDCM C++ DICOM library.

Import library
--------------

.. code:: python

    import mudicom

If GDCM and numpy have been installed successfully, there should be no issues
importing this library.

Getting list of data elements
-----------------------------

.. code:: python

    mu = mudiciom.load("dicom.dcm")
    mu.read()

Here you should see a list of DataElements, example:

.. code:: python

    [<DataElement Generic Group Length (0008,0000)>,
     <DataElement Image Type (0008,0008)>,
     <DataElement SOP Class UID (0008,0016)>,
     <DataElement SOP Instance UID (0008,0018)>,
     <DataElement Study Date (0008,0020)>]

What you get as the REPR is the name of the data element
as well as the data element tag (group, element) in hex code.
The data element tag is the unique location designation for all elements
within a DICOM file.

Searching for DICOM data elements
---------------------------------

Find data element by name
`````````````````````````

.. code:: python

    mu.find(name="Transfer Syntax UID")

The name parameter is case-insensitive so in the above example "transfer syntax uid"
works just the same.

The response will be a list of DataElements, example:

.. code:: python

    [<DataElement Transfer Syntax UID (0002,0010)>]

Find data elements by tag group
```````````````````````````````

.. code:: python

    mu.find(group=0x0002)

The response will be a list of DataElements, example:

.. code:: python

    [<DataElement File Meta Information Group Length (0002,0000)>,
     <DataElement Media Storage SOP Class UID (0002,0002)>,
     <DataElement Media Storage SOP Instance UID (0002,0003)>,
     <DataElement Transfer Syntax UID (0002,0010)>,
     <DataElement Implementation Class UID (0002,0012)>,
     <DataElement Implementation Version Name (0002,0013)>,
     <DataElement Source Application Entity Title (0002,0016)>]

You can also search for the data element by the integer value of the tag group

.. code:: python

    mu.find(group=32) # equivalent (0x020)

Find data elements by tag element
`````````````````````````````````

.. code:: python

    mu.find(element=0x0021)

The response will be a list of DataElements, example:

.. code:: python

    [<DataElement Series Date (0008,0021)>,
     <DataElement Sequence Variant (0018,0021)>]

You can also search the data element by the integer value of the tag element

.. code:: python

    mu.find(group=33) # equivalent (0x021)

And of course you can find a specific data element by specifying both the
tag group and element

.. code:: python

    mu.find(0x0002, 0x0010)

This will still return a list for consistency, even though it's only possible
to return one DataElement, example:

.. code:: python

    [<DataElement Transfer Syntax UID (0002,0010)>]

Find data elements by Value Representation (VR)
```````````````````````````````````````````````

.. code:: python

    mu.find(VR="UI")

The name parameter is case-insensitive so in the above example "ui"
works just the same.

The result will be a list of DataElements, example:

.. code:: python

    [<DataElement Media Storage SOP Class UID (0002,0002)>,
     <DataElement Media Storage SOP Instance UID (0002,0003)>,
     <DataElement Transfer Syntax UID (0002,0010)>,
     <DataElement Implementation Class UID (0002,0012)>]

Scan every GDCM DataElement and return something
------------------------------------------------

This opens up the GDCM DataElement and allows one to
gain access to other features of the object.

from GDCM, DATA ELEMENT: A unit of information as defined by a single entry in
the data dictionary. An encoded Information Object Definition (IOD)
Attribute that is composed of, at a minimum, three fields: a Data
Element Tag, a Value Length, and a Value Field. For some specific
Transfer Syntaxes, a Data Element also contains a VR Field where the
Value Representation of that Data Element is specified explicitly.

.. code:: python

    def is_empty(data_element):
        return data_element.IsEmpty()

    mu.walk(is_empty)

This returns a generator to interact with

.. code:: python

    <generator object walk at 0x10bf4b9b0>

To use the generator

.. code:: python

    [data for data in mu.walk(is_empty)]

This creates a list that has touched every GDCM DataElement in the DICOM file.

.. code:: python

    [False,
     False,
     False,
     False,
     False,
     ...]

List of methods within GDCM DataElement:

* GetTag
* SetTag
* GetVL
* SetVL
* SetVLToUndefined
* GetVR
* SetVR
* GetValue
* SetValue
* IsEmpty
* Empty
* Clear
* SetByteValue
* GetByteValue
* GetValueAsSQ
* GetSequenceOfFragments
* IsUndefinedLength

Get numpy array of DICOM image
------------------------------

Prepare the DICOM image class
`````````````````````````````

.. code:: python

    img = mu.image()

Get DICOM numpy array
`````````````````````

.. code:: python

    img.numpy()

The output will be a numpy array, example:

.. code:: python

    array([[ 1024.,  1024.,  1024., ...,  1025.,  1024.,  1024.],
           [ 1024.,  1024.,  1024., ...,  1025.,  1024.,  1024.],
           [ 1031.,  1033.,  1029., ...,  1040.,  1034.,  1028.],
           ...,
           [ 1028.,  1027.,  1027., ...,  1061.,  1025.,  1029.],
           [ 1031.,  1030.,  1030., ...,  1067.,  1026.,  1030.],
           [ 1024.,  1024.,  1024., ...,  1026.,  1024.,  1024.]])

Save DICOM as Pillow Image
--------------------------

* Requires Pillow python package

.. code:: python

    img.save_as_pil("dicom.jpg")

Save DICOM as Matplotlib Image
------------------------------

* Requires Matplotlib python package

.. code:: python

    img.save_as_plt("dicom.jpg")

Validate DICOM file
-------------------

* Requires Dicom3Tools (http://www.dclunie.com/dicom3tools.html)

.. code:: python

    mudicom.validate("dicom.dcm")

Returns dictionary conntaining errors and warnings, example:

.. code:: python

    {
        'errors': ['Missing attribute Type 2 Required Element=<PatientBirthDate> Module=<Patient>',
                   'Missing attribute Type 2 Required Element=<PatientSex> Module=<Patient>',
                   'Missing attribute Type 2 Required Element=<StudyID> Module=<GeneralStudy>',
                   'Missing attribute Type 2 Required Element=<AccessionNumber> Module=<GeneralStudy>',
                   'Missing attribute Type 2C Conditional Element=<Laterality> Module=<GeneralSeries>',
                   'A value is required for value 3 in MR Images - attribute <ImageType>'],
        'warnings': ['Bad group length - Group 0x8 specified as 0x19e actually 0x192',
                     'Bad group length - Group 0x10 specified as 0x12 actually 0x1c',
                     'Missing attribute or value that would be needed to build DICOMDIR - Study ID',
                     "Value dubious for this VR - (0x0008,0x0090) PN Referring Physician's Name  PN [0] = <anonymous> - Retired Person Name form",
                     'Value dubious for this VR - (0x0008,0x1060) PN Name of Physician(s) Reading Study  PN [0] = <anonymous> - Retired Person Name form',
                     "Value dubious for this VR - (0x0008,0x1070) PN Operators' Name  PN [0] = <anonymous> - Retired Person Name form",
                     "Value dubious for this VR - (0x0010,0x0010) PN Patient's Name  PN [0] = <anonymous> - Retired Person Name form",
                     'Retired attribute - (0x0008,0x0000) UL Group Length ',
                     'Retired attribute - (0x0010,0x0000) UL Group Length ',
                     'Retired attribute - (0x0018,0x0000) UL Group Length ',
                     'Retired attribute - (0x0020,0x0000) UL Group Length ',
                     'Retired attribute - (0x0028,0x0000) UL Group Length ',
                     'Retired attribute - (0x7fe0,0x0000) UL Group Length ',
                     'Dicom dataset contains retired attributes',
                     'Unrecognized defined term <GR> for value 1 of attribute <Sequence Variant>',
                     'Unrecognized defined term <GRAPH_GEMS> for value 1 of attribute <Scan Options>',
                     'Value is zero for value 1 of attribute <Echo Train Length>',
                     'Value is zero for value 1 of attribute <Imaging Frequency>']
    }

Look up text of Value Representation
------------------------------------

WIP

Look up value of Transfer Syntax UID
------------------------------------

WIP
