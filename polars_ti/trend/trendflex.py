# -*- coding: utf-8 -*-
from numba import njit
from numpy import cos, exp, nan, sqrt, zeros_like
from pandas import Series
from polars_ti._typing import Array, DictLike, Int, IntFloat
from polars_ti.utils import v_offset, v_pos_default, v_series


# Ehler's Trendflex
# http://traders.com/Documentation/FEEDbk_docs/2020/02/TradersTips.html
@njit(cache=True)
def nb_trendflex(x, n, k, alpha, pi, sqrt2):
    m, ratio = x.size, 2 * sqrt2 / k
    a = exp(-pi * ratio)
    b = 2 * a * cos(180 * ratio)
    c = a * a - b + 1

    _f = zeros_like(x)
    _ms = zeros_like(x)
    result = zeros_like(x)

    for i in range(2, m):
        _f[i] = 0.5 * c * (x[i] + x[i - 1]) + b * _f[i - 1] - a * a * _f[i - 2]

    for i in range(n, m):
        _sum = 0
        for j in range(1, n):
            _sum += _f[i] - _f[i - j]
        _sum /= n

        _ms[i] = alpha * _sum * _sum + (1 - alpha) * _ms[i - 1]
        if _ms[i] != 0.0:
            result[i] = _sum / sqrt(_ms[i])

    return result


def trendflex(
    close: Series,
    length: Int = None,
    smooth: Int = None,
    alpha: IntFloat = None,
    pi: IntFloat = None,
    sqrt2: IntFloat = None,
    offset: Int = None,
    **kwargs: DictLike,
) -> Series:
    """Trendflex (TRENDFLEX)

    John F. Ehlers introduced two indicators within the article "Reflex: A New
    Zero-Lag Indicator” in February 2020, TASC magazine. One of which is the
    Trendflex, a lag reduced trend indicator.
    Both indicators (Reflex/Trendflex) are oscillators and complement each
    other with the focus for cycle and trend.

    Coded by rengel8 (2021-08-11) based on the implementation on
    ProRealCode (see Sources). Beyond the mentioned source, this
    implementation has a separate control parameter for the internal applied
    SuperSmoother.

    Sources:
        http://traders.com/Documentation/FEEDbk_docs/2020/02/TradersTips.html
        https://www.prorealcode.com/prorealtime-indicators/reflex-and-trendflex-indicators-john-f-ehlers/

    Args:
        close (pd.Series): Series of 'close's
        length (int): It's period. Default: 20
        smooth (int): Period of internal SuperSmoother Default: 20
        alpha (float): Alpha weight of Difference Sums. Default: 0.04
        pi (float): The value of PI to use. The default is Ehler's
            truncated value 3.14159. Adjust the value for more precision.
            Default: 3.14159
        sqrt2 (float): The value of sqrt(2) to use. The default is Ehler's
            truncated value 1.414. Adjust the value for more precision.
            Default: 1.414
        offset (int): How many periods to offset the result. Default: 0

    Kwargs:
        fillna (value, optional): pd.DataFrame.fillna(value)

    Returns:
        pd.Series: New feature generated.
    """
    # Validate
    length = v_pos_default(length, 20)
    smooth = v_pos_default(smooth, 20)
    close = v_series(close, max(length, smooth) + 1)

    if close is None:
        return

    alpha = v_pos_default(alpha, 0.04)
    pi = v_pos_default(pi, 3.14159)
    sqrt2 = v_pos_default(sqrt2, 1.414)
    offset = v_offset(offset)

    # Calculate
    np_close = close.to_numpy()
    result = nb_trendflex(np_close, length, smooth, alpha, pi, sqrt2)
    result[:length] = nan
    result = Series(result, index=close.index)

    # Offset
    if offset != 0:
        result = result.shift(offset)

    # Fill
    if "fillna" in kwargs:
        result.fillna(kwargs["fillna"], inplace=True)

    # Name and Category
    result.name = f"TRENDFLEX_{length}_{smooth}_{alpha}"
    result.category = "trend"

    return result
