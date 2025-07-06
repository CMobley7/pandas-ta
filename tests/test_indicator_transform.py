# -*- coding: utf-8 -*-
import polars_ti as ti


# TA Lib style Tests
def test_cube(df):
    result = ti.cube(df.close)
    assert result.name == "CUBE_3.0_-1"


def test_ifisher(df):
    result = ti.ifisher(df.close)
    assert result.name == "INVFISHER_1.0"


def test_remap(df):
    result = ti.remap(df.close)
    assert result.name == "REMAP_0.0_100.0_-1.0_1.0"


# DataFrame Extension Tests
def test_ext_cube(df):
    df.ti.cube(append=True)
    assert list(df.columns[-2:]) == ["CUBE_3.0_-1", "CUBEs_3.0_-1"]


def test_ext_ifisher(df):
    df.ti.ifisher(append=True)
    assert list(df.columns[-2:]) == ["INVFISHER_1.0", "INVFISHERs_1.0"]


def test_ext_remap(df):
    df.ti.remap(append=True)
    assert df.columns[-1] == "REMAP_0.0_100.0_-1.0_1.0"
