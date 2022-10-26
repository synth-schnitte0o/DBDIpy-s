# DBDIpy (Version 0.7.0)

DBDIpy is an open-source Python library for the curation and interpretation of dielectric barrier discharge ionisation mass spectrometric datasets.

# tl;dr
1. [Installation](#installation)
2. [User Tutorial](#tutorial)

# Introduction

Mass spectrometric data from direct injection analysis is hard to interprete as missing chromatographic separation complicates identification of fragments and adducts generated during the ionization process.

Here we present an *in-silico* approach to putatively identify multiple ion species arising from one analyte compound specially tailored for time-resolved datasets from dielectric barrier dischardge ionization (DBDI). DBDI is a relatively young technology which is rapidly gaining popularity in applications as breath analysis, process controll or food research. 

DBDIpy's core functionality relys on putative identification of in-source fragments (eg. [M-H<sub>2</sub>O+H]<sup>+</sup>) and in-source generated adducts (eg. [M+<sub>n</sub>O+H]<sup>+</sup>). 
Custom adduct species can be defined by the user and passed to this open-search algorithm. The identification is performed in a two-step procedure: 
- calculation of pointwise correlation identifies features with matching temporal intensity profiles through the experiment.
- (exact) mass differences are used to define the nature of potential candidates. 

These putative identifications can than further be validated by the user, eg. based on tandem MS fragment data.               

DBDIpy further comes along with functions optimized for preprocessing of experimental data and visualization of identified adducts. The library is integrated into the matchms ecosystem to assimilate DBDIpy's functionalities into existing workflows.

For details, we invite you to read the [tutorial](#tutorial) or to try out the functions with our [demonstrational dataset](https://doi.org/10.5281/zenodo.7221089) or your own data!


|                     | Badges                                                                             |
|:-------------       |:-----------------------------------------------------------------------------------|
| `License`           | [![PyPi license](https://badgen.net/pypi/license/pip/)]([https://pypi.com/project/pip/](https://opensource.org/licenses/MIT/))|
| `Status`            | [![test](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/leopold-weidner/DBDIpy/graphs/commit-activity)|
| `Updated`           | [![GitHub latest commit](https://badgen.net/github/last-commit/Naereen/Strapdown.js)](https://GitHub.com/leopold-weidner/DBDIpy/commit/)|
| `Language`          | [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)|
| `Version`           | [![Python - 3.7, 3.8, 3.9, 3.10](https://img.shields.io/static/v1?label=Python&message=3.7+,+3.8+,+3.9+,+3.10&color=2d4b65)](https://www.python.org/)|
| `Operating Systems` | [![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg) [![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)|
| `Documentation`     | [![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/leopold-weidner/DBDIpy)|
| `Supporting Data`   | [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7221089.svg)](https://doi.org/10.5281/zenodo.7221089)|
| `Further Reads`     | [![Researchgate](https://img.shields.io/badge/Research_Gate-00CCBB.svg?&style=for-the-badge&logo=ResearchGate&logoColor=white)](https://www.researchgate.net/profile/Leopold-Weidner)|


Latest Changes (since 0.6.0)
------------
- updated description.
- improved help pages.
- began writing tutorial.


User guide
============

## Installation

Prerequisites:  

- Anaconda (recommended)
- Python 3.7, 3.8, 3.9 or 3.10

DBDIpy can be instaled from PyPI  with:

```python
# we recomend installing DBDIpy in a new virtual environment
conda create --name DBDIpy python=3.9
conda activate DBDIpy
python3 -m pip install DBDIpy
```


Known installation issues:
Apple M1 chip users might encounter issues with automatic installation of matchms. 
Manual installation of the dependency as described on the libraries [official site](https://github.com/matchms/matchms) helps solving the issue. 
  

## Tutorial

...further text ...



Contact
============
leopold.weidner@tum.de
