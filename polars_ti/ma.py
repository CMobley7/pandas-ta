# -*- coding: utf-8 -*-
from pandas import Series

from polars_ti._typing import DictLike
from polars_ti.overlap.dema import dema
from polars_ti.overlap.ema import ema
from polars_ti.overlap.fwma import fwma
from polars_ti.overlap.hma import hma
from polars_ti.overlap.linreg import linreg
from polars_ti.overlap.midpoint import midpoint
from polars_ti.overlap.pwma import pwma
from polars_ti.overlap.rma import rma
from polars_ti.overlap.sinwma import sinwma
from polars_ti.overlap.sma import sma
from polars_ti.overlap.ssf import ssf
from polars_ti.overlap.swma import swma
from polars_ti.overlap.t3 import t3
from polars_ti.overlap.tema import tema
from polars_ti.overlap.trima import trima
from polars_ti.overlap.vidya import vidya
from polars_ti.overlap.wma import wma


def ma(name: str = None, source: Series = None, **kwargs: DictLike) -> Series:
    """Simple MA Utility for easier MA selection

    Available MAs:
        dema, ema, fwma, hma, linreg, midpoint, pwma, rma, sinwma, sma, ssf,
        swma, t3, tema, trima, vidya, wma

    Examples:
        ema8 = ti.ma("ema", df.close, length=8)
        sma50 = ti.ma("sma", df.close, length=50)
        pwma10 = ti.ma("pwma", df.close, length=10, asc=False)

    Args:
        name (str): One of the Available MAs. Default: "ema"
        source (pd.Series): The 'source' Series.

    Kwargs:
        Any additional kwargs the MA may require.

    Returns:
        pd.Series: New feature generated.
    """
    _mas = [
        "dema",
        "ema",
        "fwma",
        "hma",
        "linreg",
        "midpoint",
        "pwma",
        "rma",
        "sinwma",
        "sma",
        "ssf",
        "swma",
        "t3",
        "tema",
        "trima",
        "vidya",
        "wma",
    ]
    if name is None and source is None:
        return _mas
    elif isinstance(name, str) and name.lower() in _mas:
        name = name.lower()
    else:  # "ema"
        name = _mas[1]

    if name == "dema":
        return dema(source, **kwargs)
    elif name == "fwma":
        return fwma(source, **kwargs)
    elif name == "hma":
        return hma(source, **kwargs)
    elif name == "linreg":
        return linreg(source, **kwargs)
    elif name == "midpoint":
        return midpoint(source, **kwargs)
    elif name == "pwma":
        return pwma(source, **kwargs)
    elif name == "rma":
        return rma(source, **kwargs)
    elif name == "sinwma":
        return sinwma(source, **kwargs)
    elif name == "sma":
        return sma(source, **kwargs)
    elif name == "ssf":
        return ssf(source, **kwargs)
    elif name == "swma":
        return swma(source, **kwargs)
    elif name == "t3":
        return t3(source, **kwargs)
    elif name == "tema":
        return tema(source, **kwargs)
    elif name == "trima":
        return trima(source, **kwargs)
    elif name == "vidya":
        return vidya(source, **kwargs)
    elif name == "wma":
        return wma(source, **kwargs)
    else:
        return ema(source, **kwargs)
