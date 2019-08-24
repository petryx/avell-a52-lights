from setuptools import setup, find_packages
from codecs import open
from os import path
import os

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

packages = [
        'avell_a52',
        'avell_a52.driver',
]



setup(
    name='avell_a52',
    version='1.0.2',
    description='A Project to provide a driver and interface to control keyboard rgb led of ITE 8291 V0.2 like Avell laptops',
    scripts=['avell_a52/lightkeys'],
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/petryx/avell-a52-lights', 
    author='Petryx',
    author_email='marlonpetry@gmail.com',
    packages=packages,
    install_requires=[
	'pyusb',
	],
    project_urls={
        'Bug Reports': 'https://github.com/petryx/avell-a52-lights/issues',
        'Source': 'https://github.com/petryx/avell-a52-lights',
    },
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: POSIX :: Linux",
    ],
)
