import re
from setuptools import setup, find_packages

def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
	name='mudicom',
	version='0.0.2',
	author='Eric Bower',
	author_email='neurosnap@gmail.com',
	packages=find_packages(),
	url='https://github.com/neurosnap/mudicom',
	license=read('LICENSE.rst'),
	description='Read and extract images from a DICOM file using GDCM',
    long_description=read('README.rst') + '\n\n' + read('CHANGES.rst'),
    tests_require=['nosetest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License'
    ],
    keywords=['dicom', 'gdcm', 'imaging', 'medical', 'images']
)
