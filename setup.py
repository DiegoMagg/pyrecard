import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrecard",
    version="0.0.2",
    author="Diego Magalhães",
    author_email="dmlmagal@gmail.com",
    description="A Python package for wirecard payment gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/pyrecard",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
