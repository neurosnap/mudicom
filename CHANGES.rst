Change Log
==========

v0.1.0, 1-11-2015
------------------

- Re-organized package modules
- Added \__version\__ variable
- Added and updated unit tests
- mudicom.load() now accepts kwargs
- Dicom() has new method: validate()
- Dicom() has new attributes: errors, warnings, image
- mudicom.base.Dicom.image is now an attribute, breaks backwards compat
- mudicom.image.Image.numpy is now an attribute, breaks backwards compat
- Added mudicom.exceptions module with InvalidDicom exception

v0.0.9, 10-19-2014
------------------

- Added basic profile DICOM anonymization
- Added ability to save changes to DICOM file, "save as"

v0.0.8, 10-17-2014
------------------

- Fixed another python 3 issue with unit tests
- Added guide on basic usage
- Added str and repr properties to primary classes
- Ramped up documentation at http://mudicom.dcmdb.org/

v0.0.7, 10-16-2014
------------------

- Fixed python 3 issue with GDCM image encoding

v0.0.6, 09-08-2014
------------------

- Updated README for clarity
- Created bried roadmap

v0.0.5, 08-14-2014
------------------

- Updated MANIFEST.in to include .rst, I'm a dumbass

v0.0.4, 08-14-2014
------------------

- Removed LICENSE.rst from setup.py

v0.0.3, 08-14-2014
------------------

- PIP cannot read LICENSE.rst for some reason

v0.0.3, 08-14-2014
------------------

- Weird permission issues with the egg

v0.0.2, 08-14-2014
------------------

- Updated packaging description

v0.0.1, 04-04-2014
------------------

- Initial release.