from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.01'
DESCRIPTION = 'Work with fiscal calendar with a 52/53 structure'
LONG_DESCRIPTION = 'Some fiscal calendars have a 52/53 week year, and this particular one always starts on Saturday and ends on Friday'

# Setting up
setup(
    name="fiscal5253",
    version=VERSION,
    author="Kristofer Pelletier",
    author_email="<kristofer.pelletier@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['datetime', 'calendar'],
    keywords=['python', 'date', 'fiscal', '5253'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)