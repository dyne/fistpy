from setuptools import setup, find_packages

VERSION = (0, 0, 4)
__version__ = VERSION
__version_str__ = ".".join(map(str, VERSION))

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="fistpy",
    version=__version_str__,
    author="Puria Nafisi Azizi",
    author_email="puria@dyne.org",
    description="Python wrapper for the FIST full-text index serve",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/dyne/fistpy",
    license="Apache 2.0",
    packages=find_packages(),
    install_requires=["pre-commit==1.14.4", "pytest_runner==4.4"],
    tests_require=["pytest", "codecov", "pytest-cov", "pytest-mock"],
    python_requires=">3.5",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
