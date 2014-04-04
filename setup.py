import re
from setuptools import setup, find_packages

def find_version(fname):
	'''Attempts to find the version number in the file names fname.
	Raises RuntimeError if not found.
	'''
	version = ''
	with open(fname, 'r') as fp:
		reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
		for line in fp:
			m = reg.match(line)
			if m:
				version = m.group(1)
				break
	if not version:
		raise RuntimeError('Cannot find version information')
	return version

__version__ = find_version('dicomimg/__init__.py')

setup(
	name='DicomImg',
	version=__version__,
	author='Eric Bower',
	author_email='neurosnap@gmail.com',
	packages=find_packages(),
	url='http://pypi.python.org/pypi/DicomImg/',
	license='LICENSE',
)