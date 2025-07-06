"""
.. moduleauthor:: Christopher Mobley
"""

name = "polars_ti"

# Flat Structure. Supports ti.ema() or ti.overlap.ema() calls.
from polars_ti.candles import *
from polars_ti.candles import __all__ as candles_all

# Enable "ti" DataFrame Extension
from polars_ti.core import TechnicalIndicators

# Custom External Directory Commands. See help(import_dir)
from polars_ti.custom import create_dir, import_dir
from polars_ti.cycles import *
from polars_ti.cycles import __all__ as cycles_all

# Common Averages useful for Indicators
# with a mamode argument, like ti.adx()
from polars_ti.ma import ma

# Dictionaries and version
from polars_ti.maps import EXCHANGE_TZ, RATE, Category, Imports, version
from polars_ti.momentum import *
from polars_ti.momentum import __all__ as momentum_all
from polars_ti.overlap import *
from polars_ti.overlap import __all__ as overlap_all
from polars_ti.performance import *
from polars_ti.performance import __all__ as performance_all
from polars_ti.statistics import *
from polars_ti.statistics import __all__ as statistics_all
from polars_ti.transform import *
from polars_ti.transform import __all__ as transform_all
from polars_ti.trend import *
from polars_ti.trend import __all__ as trend_all
from polars_ti.utils import *
from polars_ti.utils import __all__ as utils_all
from polars_ti.volatility import *
from polars_ti.volatility import __all__ as volatility_all
from polars_ti.volume import *
from polars_ti.volume import __all__ as volume_all

__all__ = [
    "name",
    "EXCHANGE_TZ",
    "RATE",
    "Category",
    "Imports",
    "version",
    "ma",
    "create_dir",
    "import_dir",
    "TechnicalIndicators",
]

__all__ += [
    utils_all
    + candles_all
    + cycles_all
    + momentum_all
    + overlap_all
    + performance_all
    + statistics_all
    + transform_all
    + trend_all
    + volatility_all
    + volume_all
]
