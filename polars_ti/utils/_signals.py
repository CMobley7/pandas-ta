# -*- coding: utf-8 -*-
from pandas import DataFrame, Series
from polars_ti._typing import DictLike, Int, IntFloat
from polars_ti.utils._math import zero
from polars_ti.utils._validate import v_offset, v_series


def _above_below(
    series_a: Series,
    series_b: Series,
    above: bool = True,
    asint: bool = True,
    offset: Int = None,
    **kwargs,
) -> Series:
    # Verify
    series_a = v_series(series_a)
    series_b = v_series(series_b)
    offset = v_offset(offset)

    series_a.apply(zero)
    series_b.apply(zero)

    # Calculate
    if above:
        current = series_a >= series_b
    else:
        current = series_a <= series_b

    if asint:
        current = current.astype(int)

    # Offset
    if offset != 0:
        current = current.shift(offset)

    # Name and Category
    current.name = f"{series_a.name}_{'A' if above else 'B'}_{series_b.name}"
    current.category = "utility"

    return current


def above(
    series_a: Series, series_b: Series, asint: bool = True, offset: Int = None, **kwargs
) -> Series:
    return _above_below(
        series_a, series_b, above=True, asint=asint, offset=offset, **kwargs
    )


def above_value(
    series_a: Series, value: IntFloat, asint: bool = True, offset: Int = None, **kwargs
) -> Series:
    if not isinstance(value, (int, float, complex)):
        print("[X] value is not a number")
        return
    series_b = Series(value, index=series_a.index, name=f"{value}".replace(".", "_"))

    return _above_below(
        series_a, series_b, above=True, asint=asint, offset=offset, **kwargs
    )


def below(
    series_a: Series, series_b: Series, asint: bool = True, offset: Int = None, **kwargs
) -> Series:
    return _above_below(
        series_a, series_b, above=False, asint=asint, offset=offset, **kwargs
    )


def below_value(
    series_a: Series, value: IntFloat, asint: bool = True, offset: Int = None, **kwargs
) -> Series:
    if not isinstance(value, (int, float, complex)):
        print("[X] value is not a number")
        return
    series_b = Series(value, index=series_a.index, name=f"{value}".replace(".", "_"))
    return _above_below(
        series_a, series_b, above=False, asint=asint, offset=offset, **kwargs
    )


def cross_value(
    series_a: Series,
    value: IntFloat,
    above: bool = True,
    equal: bool = True,
    asint: bool = True,
    offset: Int = None,
    **kwargs,
) -> Series:
    series_b = Series(value, index=series_a.index, name=f"{value}".replace(".", "_"))

    return cross(series_a, series_b, above, equal, asint, offset, **kwargs)


def cross(
    series_a: Series,
    series_b: Series,
    above: bool = True,
    equal: bool = True,
    asint: bool = True,
    offset: Int = None,
    **kwargs: DictLike,
) -> Series:
    # Validate
    series_a = v_series(series_a)
    series_b = v_series(series_b)
    offset = v_offset(offset)

    series_a.apply(zero)
    series_b.apply(zero)

    # Calculate
    if above:
        current = series_a >= series_b if equal else series_a > series_b
        previous = series_a.shift(1) < series_b.shift(1)
    else:
        current = series_a <= series_b if equal else series_a < series_b
        previous = series_a.shift(1) > series_b.shift(1)

    cross = current & previous
    # ensure there is no cross on the first entry
    cross.iloc[0] = False

    if asint:
        cross = cross.astype(int)

    # Offset
    if offset != 0:
        cross = cross.shift(offset)

    # Name and Category
    cross.name = f"{series_a.name}_{'XA' if above else 'XB'}_{series_b.name}"
    cross.category = "utility"

    return cross


def signals(
    indicator: Series,
    xa: IntFloat,
    xb: IntFloat,
    cross_values: bool,
    xserie: Series,
    xserie_a: Series,
    xserie_b: Series,
    cross_series: bool,
    offset: Int,
) -> DataFrame:

    df = DataFrame()
    if xa is not None and isinstance(xa, (int, float)):
        if cross_values:
            crossed_above_start = cross_value(indicator, xa, above=True, offset=offset)
            crossed_above_end = cross_value(indicator, xa, above=False, offset=offset)
            df[crossed_above_start.name] = crossed_above_start
            df[crossed_above_end.name] = crossed_above_end
        else:
            crossed_above = above_value(indicator, xa, offset=offset)
            df[crossed_above.name] = crossed_above

    if xb is not None and isinstance(xb, (int, float)):
        if cross_values:
            crossed_below_start = cross_value(indicator, xb, above=True, offset=offset)
            crossed_below_end = cross_value(indicator, xb, above=False, offset=offset)
            df[crossed_below_start.name] = crossed_below_start
            df[crossed_below_end.name] = crossed_below_end
        else:
            crossed_below = below_value(indicator, xb, offset=offset)
            df[crossed_below.name] = crossed_below

    # xseries is the default value for both xserie_a and xserie_b
    if xserie_a is None:
        xserie_a = xserie
    if xserie_b is None:
        xserie_b = xserie

    if xserie_a is not None and v_series(xserie_a):
        if cross_series:
            cross_serie_above = cross(indicator, xserie_a, above=True, offset=offset)
        else:
            cross_serie_above = above(indicator, xserie_a, offset=offset)

        df[cross_serie_above.name] = cross_serie_above

    if xserie_b is not None and v_series(xserie_b):
        if cross_series:
            cross_serie_below = cross(indicator, xserie_b, above=False, offset=offset)
        else:
            cross_serie_below = below(indicator, xserie_b, offset=offset)

        df[cross_serie_below.name] = cross_serie_below

    return df
