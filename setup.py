
import os
from setuptools import setup
from expirecache import __version__

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'expirecache',
    packages = ['expirecache'],
    version = __version__,
    author = 'Kael Zhang',
    author_email = 'i@kael.me',
    description = ('A process-safe python adapter to handle cache expiration.'),
    license = 'MIT',
    keywords = 'cache python expire memcached',
    url = 'https://github.com/kaelzhang/python-expire-cache',
    long_description=read('README.rst'),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ]
)
