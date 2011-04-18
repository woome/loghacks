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
    description = "virtualenv for hg",
    long_description = """Tie virtualenvs to individual mercurial repositorys.""",
    license = "GNU GPL v3",
    author = "Nic Ferrier",
    author_email = "nic@ferrier.me.uk",
    url = "http://github.com/woome/loghacks",
    download_url="http://github.com/woome/loghacks/downloads",
    platforms = ["any"],
    packages=['loghacks'],
    classifiers =  classifiers,
    )
