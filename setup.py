import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="liteevent",
    version="1.0.0",
    description="A decorator-based, lightweight event library for Python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DarkWolf2244/LiteEvent",
    author="DarkWolf",
    author_email="darkwolfx2244@gmail.com",
    license="GNU General Public License v3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=[],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            
        ]
    },
)