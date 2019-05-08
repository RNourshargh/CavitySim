import versioneer

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


PACKAGE_NAME = "cavitysim"
AUTHOR = "Rustin Nourshargh"
EMAIL = "rustin@hotmail.co.uk"
URL = "https://github.com/RNourshargh/CavitySimMatlab"

DESCRIPTION = "Simulation of different optical cavities using ABCD matricies from the constituent optical components."
README = "README.md"

SOURCE_DIR = "src"

with open(README, "r") as readme_file:
    README_TEXT = readme_file.read()


class CavitySim(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        pytest.main(self.test_args)


cmdclass = versioneer.get_cmdclass()
cmdclass.update({"test": CavitySim})

setup(
    name=PACKAGE_NAME,
    version=versioneer.get_version(),
    description=DESCRIPTION,
    long_description=README_TEXT,
    long_description_content_type="text/md",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    # license="2-Clause BSD License",
    # classifiers=[
    #     "Development Status :: 4 - Beta",
    #     "License :: OSI Approved :: BSD License",
    #     "Intended Audience :: Developers",
    #     "Operating System :: OS Independent",
    #     "Programming Language :: Python :: 3.6",
    # ],
    keywords=["optical", "cavity", "simulation", "abcd"],
    packages=find_packages(SOURCE_DIR),  # no tests/docs in `src` so don't need exclude
    package_dir={"": SOURCE_DIR},
    install_requires=["numpy", "matplotlib"],
    extras_require={
        "docs": ["sphinx", "sphinx_rtd_theme"],
        "test": ["codecov", "pytest-cov", "pytest"],
        "deploy": ["twine", "setuptools", "wheel", "flake8", "black", "versioneer"],
    },
    cmdclass=cmdclass,
)
