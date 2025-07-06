# -*- coding: utf-8 -*-
import polars_ti as ti


# TA Lib style Tests
def test_drawdown(df):
    result = ti.drawdown(df.close)
    assert result.name == "DD"


def test_log_return(df):
    result = ti.log_return(df.close)
    assert result.name == "LOGRET_1"


def test_cumlog_return(df):
    result = ti.log_return(df.close, cumulative=True)
    assert result.name == "CUMLOGRET_1"


def test_percent_return(df):
    result = ti.percent_return(df.close, cumulative=False)
    assert result.name == "PCTRET_1"


def test_cumpercent_return(df):
    result = ti.percent_return(df.close, cumulative=True)
    assert result.name == "CUMPCTRET_1"


# DataFrame Extension Tests
def test_ext_log_return(df):
    df.ti.log_return(append=True)
    assert df.columns[-1] == "LOGRET_1"


def test_ext_cumlog_return(df):
    df.ti.log_return(cumulative=True, append=True)
    assert df.columns[-1] == "CUMLOGRET_1"


def test_ext_percent_return(df):
    df.ti.percent_return(append=True)
    assert df.columns[-1] == "PCTRET_1"


def test_ext_cumpercent_return(df):
    df.ti.percent_return(cumulative=True, append=True)
    assert df.columns[-1] == "CUMPCTRET_1"
