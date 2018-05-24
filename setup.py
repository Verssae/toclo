"""Packaging settings."""


# from codecs import open
from os.path import abspath, dirname, join


from setuptools import Command, find_packages, setup

from toclo import __version__


this_dir = abspath(dirname(__file__))
# with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
#     long_description = file.read()

setup(
    name = 'toclo',
    version = __version__,
    description = 'A todo list command line program in Python.',
    # long_description = long_description,
    url = "https://github.com/Verssae/toclo",
    download_url = 'https://github.com/Verssae/toclo.git',
    author = 'Verssae',
    author_email = 'sparky@hanynag.ac.kr',
    license = 'MIT',
    classifiers = [
        # 'Intended Audience :: Developers',
        # 'Topic :: Utilities',
        # 'License :: Public Domain',
        # 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'todolist',
    packages = find_packages(exclude=['docs']),
    install_requires = ['docopt','colorama'],
    
    entry_points = {
        'console_scripts': [
            'toclo=toclo.cli:main',
        ],
    }
    
)
