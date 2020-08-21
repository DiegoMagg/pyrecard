import setuptools
from pyrecard.__version__ import (
    __version__,
    __author__,
    __author_email__,
    __description__,
    __url__,
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrecard",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__url__,
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
