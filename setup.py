from setuptools import setup

from loghacks import __version__

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities',
]

setup(
    name = "loghacks",
    version = __version__,
    description = "python logging utility for django projects",
    long_description = """custom logging package for django.""",
    license = "GNU GPL v3",
    author = "Otu Ekanem",
    author_email = "io2@woome.com",
    url = "http://github.com/woome/loghacks",
    download_url = "http://github.com/woome/loghacks/tarball/master",
    platforms = ["any"],
    packages = ['loghacks'],
    classifiers =  classifiers,
    )
