import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="liteevent",
    version="1.0.0",
    description="A decorator-based, lightweight event library for Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DarkWolf2244/LiteEvent",
    author="DarkWolf",
    author_email="darkwolfx2244@gmail.com",
    license="GNU GPLv3",
    classifiers=[
        "License :: GNU GPLv3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            
        ]
    },
)