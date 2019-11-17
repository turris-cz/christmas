#!/usr/bin/env python3

from setuptools import setup, find_packages

from christmas import __version__


setup(
        name="christmas",
        version=__version__,
        description="Christmas - Shine Turris router like a Christmas tree",
        author="CZ.NIC, z.s.p.o.",
        author_email="packaging@turris.cz",
        license='GNU GPL v3',
        url="https://gitlab.labs.nic.cz/turris/sentinel/sview",
        packages=find_packages(),
        install_requires=[
            "pyuci",
        ],
        entry_points={
            'console_scripts': [
                'christmas=christmas.__main__:main'
            ]
        },
)
