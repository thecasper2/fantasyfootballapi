from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fantasyprem",
    version="0.0.1",
    author="Alex Dolphin",
    author_email="",
    description="A package to handle data from the Premier League Fantasy Football API",
    install_requires=[
        "pytest >= 4.0.2"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.5",
    setup_requires=[
        "pytest-runner",
        "pandas >= 0.24.2",
        "requests >= 2.22.0"
    ],
    tests_require=[
        "pytest",
        "pytest-cov"
    ]
)
