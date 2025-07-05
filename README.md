<p align="center">
  <a href="https://www.pandas-ta.dev"><img src="images/ta-logo.png" alt="Pandas TA"></a>
</p>

# Pandas TA
### A Comprehensive Python Technical Analysis Library for Traders and Investors

[![license](https://img.shields.io/github/license/twopirllc/pandas-ta)](#license)
[![Python Version](https://img.shields.io/pypi/pyversions/pandas-ta?style=flat)](https://pypi.org/project/pandas_ta/)
[![PyPi Version](https://img.shields.io/pypi/v/pandas-ta?style=flat)](https://pypi.org/project/pandas_ta/)
[![Package Status](https://img.shields.io/pypi/status/pandas-ta?style=flat)](https://pypi.org/project/pandas_ta/)
[![Downloads](https://img.shields.io/pypi/dm/pandas_ta?style=flat)](https://pypistats.org/packages/pandas_ta)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pandas-ta.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/pandas-ta)
[![Stars](https://img.shields.io/github/stars/twopirllc/pandas-ta?style=flat)](#stars)
[![Forks](https://img.shields.io/github/forks/twopirllc/pandas-ta?style=flat)](#forks)
[![Used By](https://img.shields.io/badge/used_by-258-orange.svg?style=flat)](#usedby)
[![Contributors](https://img.shields.io/github/contributors/twopirllc/pandas-ta?style=flat)](#contributors)
[![Issues](https://img.shields.io/github/issues-raw/twopirllc/pandas-ta?style=flat)](#issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/twopirllc/pandas-ta?style=flat)](#closed-issues)
[![Buy Me a Coffee](https://img.shields.io/badge/buy_me_a_coffee-orange.svg?style=flat)](https://www.buymeacoffee.com/twopirllc)

# Description

_Pandas Technical Analysis_ ([Pandas TA](https://www.pandas-ta.dev)) is a Popular Comprehensive and Easy to Use Python 3 Technical Analysis Library with primary dependencies: _numpy_ for accuracy, _numba_ for performance, and _pandas_ for brevity and bulk processing.

![Example Chart](/images/SPY_Chart.png)
![Example Chart](/images/SPY_VOL.png)

<br>


## Features
* A Free & Open Source library with a LARGE flat library structure similar to TA Lib.
  * [150+ indicators](https://www.pandas-ta.dev) and utilities.
  * [60+ Candelstick Patterns](https://www.pandas-ta.dev) with [TA Lib](https://ta-lib.org/) installed.
* Performance improvements with [numba](https://github.com/numba/numba)
* A [Pandas DataFrame Extension](https://pandas.pydata.org/docs/development/extending.html) named "ta", that provides additional properties, methods, and indicators to simplify time series calculations of ```ohlcv``` columns.
* Indicator Equivalence
  * **Primarily:** TA Lib
  * **Secondarily:** TradingView
  * **Tertiary:** [Sierra Chart](https://search.sierrachart.com/?Query=indicators&submitted=true) | [MQL5](https://www.mql5.com) | [FM Labs](https://www.fmlabs.com/reference/default.htm) | [Pro Real Code](https://www.prorealcode.com/prorealtime-indicators) | [User 42](https://user42.tuxfamily.org/chart/manual/index.html) | [Technical Traders](http://technical.traders.com/tradersonline/FeedTT-2014.html) | etc
* And [more ...](https://www.pandas-ta.dev/#features)

<br>

## About Churn
The **state** and **status** of this library and it's slowversioning increments _seem_ to be having an impact on it's long term viability and support.

This adapted variation from [Intercooler JS](https://intercoolerjs.org/docs#conclusion) clarifies  why Pandas TA does not have frequent versioning.

"This is not because it is dead, but rather because it is (mostly) right: the basic idea is right, and the implementation at least right enough.

Thus there will not be constant activity and churn on the project, but rather a stewardship relationship, where the main goal now is to not screw it up. Documentation and testing will be improved, features/indicators will be added/removed as needed, but there will be no massive rewrite or constant updating. This is in contrast with the software industry in general, which often has comical levels of churn."

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=twopirllc/pandas-ta&type=Date&theme=dark" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=twopirllc/pandas-ta&type=Date" />
  <img alt="Pandas TA Project Star History Chart" src="https://api.star-history.com/svg?repos=twopirllc/pandas-ta&type=Date" />
</picture>

<br>


# Support :broken_heart:
**A big thank you to all current and past sponsors, whose generous support has been and continues to be essential to the success of the project!** :pray:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/twopirllc) [![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K4ZRH9D)

Despite what the usage metrics indicate, current and past levels of support are **unsustainable** for maintaining and improving the library. Unless  significant additional support is provided by _July 1st, 2026_, this widely used library will be **archived**. Support through [contributions](https://github.com/twopirllc/pandas-ta/labels/help%20wanted), [donations](https://www.buymeacoffee.com/twopirllc) & [sponsorships](https://github.com/twopirllc) is **necessary** to ensure the project's continued success and development.

:stop_sign: Please* **DO NOT** email me personally with Pandas TA Bugs, Issues or Feature Requests that are best handled via Github [Issues](https://github.com/twopirllc/pandas-ta/issues).

<br>


# Installation
Before installing, review the installation [requirements.txt](https://github.com/twopirllc/pandas-ta/requirements.txt) to ensure your system is set up properly.

### From pypi
```sh
$ pip install pandas-ta
```

### From Github
```sh
$ pip install git+https://github.com/twopirllc/pandas-ta
```

### Development Version
```sh
$ pip install -U git+https://github.com/twopirllc/pandas-ta.git@development
```
* The _development_ version includes _numerous_ bug fixes, speed improvements and better documentation since release, _0.3.14b_.

### Local Installation
Click on green [<> Code](https://github.com/twopirllc/pandas-ta) button to download the source zip and unzip in your application directory. Then perform a local install.

<br>


# Bugs, Indicators and Feature Requests
* Some bugs and features may already be fixed or implemented in the _development_ version. _Please_ try the _development_ version first **before** making an issue!
* If the _development_ version does not resolve the bug, search both _Open_ and _Closed_ [Issues](https://github.com/twopirllc/pandas-ta/issues) **before** opening a new Issue.

<br>


# Contributors
Thank you all for your help! It has been and continues to be integral to this project. :sunglasses:

<br>

<a href="https://github.com/twopirllc/pandas-ta/graphs/contributors">
  <img src="https://contrib.rocks/image?anon=1&repo=twopirllc/pandas-ta" noZoom />
</a>

Made with [contrib.rocks](https://contrib.rocks).

<br>


# Contributing
Anyone who wishes to contribute to this project - be it documentation, features, bug fixes, code cleanup, testing, open issue help, or code reviews - are encouraged to do so. These contributions are crucial to the longevity of this project.

Based on your skill level, select from the following issue topics:

[Good First Issue](https://github.com/twopirllc/pandas-ta/labels/good%20first%20issue) | [Bugs](https://github.com/twopirllc/pandas-ta/labels/bug) | [Help Wanted](https://github.com/twopirllc/pandas-ta/labels/help%20wanted) | [Enhancements](https://github.com/twopirllc/pandas-ta/labels/enhancement)

<br>


# Code of Conduct
See the [Code of Conduct](https://github.com/twopirllc/pandas-ta?tab=coc-ov-file) regarding handling yourself and dealing with others in and around the Pandas TA community. Ensure you completely understand the "common sense" **Guidelines** outlined there.

<br>


# License
[MIT](https://github.com/twopirllc/pandas-ta/LICENSE)

<br>

Copyright © 2024 - Pandas TA
