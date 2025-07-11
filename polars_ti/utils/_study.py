# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from multiprocessing import cpu_count

from polars_ti._typing import Int, List
from polars_ti.utils._time import get_time


# Study DataClass
@dataclass
class Study:
    """Study DataClass
    Class to name and group indicators for processing

    Args:
        name (str): Some short memorable string.
            Note: Case-insensitive "All" is reserved.
        ti (list of dicts): A list of dicts containing keyword arguments
            where "kind" is the indicator.
        cores (int): The number cores to use for the study().
            Default: cpu_count()
        description (str): A more detailed description of what the Study
            tries to capture. Default: None
        created (str): At datetime string of when it was created.
            Default: Automatically generated. *Subject to change*

    Example TI:
    ti = [
        {"kind": "sma", "length": 200},
        {"kind": "sma", "close": "volume", "length": 50},
        {"kind": "bbands", "length": 20},
        {"kind": "rsi"},
        {"kind": "macd", "fast": 8, "slow": 21},
        {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME"},
    ],
    """

    name: str  # = None # Required.
    ti: List = field(default_factory=list)  # Required.
    cores: Int = cpu_count()  # Number of cores. Default cpu_count()
    description: str = ""  # Helpful. More descriptive version or notes or w/e.
    # Optional. Gets Exchange Time and Local Time execution time
    created: str = get_time(to_string=True)

    def __post_init__(self):
        if (
            isinstance(self.cores, int)
            and self.cores >= 0
            and self.cores <= cpu_count()
        ):
            self.cores = int(self.cores)

        req_args = ["[X] Study requires the following argument(s):"]

        if self._is_name():
            req_args.append(
                ' - name. Must be a string. Example: "My TI". Note: "all" is reserved.'
            )

        if self.ti is None:
            self.ti = None
        elif not self._is_ti():
            s = " - ti. Format is a list of dicts. Example: [{'kind': 'sma', 'length': 10}]"
            s += "\n       Check the indicator for the correct arguments if you receive this error."
            req_args.append(s)

        if len(req_args) > 1:
            [print(_) for _ in req_args]
            return None

    def _is_name(self):
        return self.name is None or not isinstance(self.name, str)

    def _is_ti(self):
        if isinstance(self.ti, list) and self.total_ti() > 0:
            # Check that all elements of the list are dicts.
            # Does not check if the dicts values are valid indicator kwargs
            # User must check indicator documentation for all indicators args.
            return all([isinstance(_, dict) and len(_.keys()) > 0 for _ in self.ti])
        return False

    def total_ti(self):
        return len(self.ti) if self.ti is not None else 0


# All Study
AllStudy = Study(
    name="All",
    description="All the indicators with their default settings. Polars TI default.",
    ti=None,
)

# Default (Example) Study.
CommonStudy = Study(
    name="Common Price and Volume SMAs",
    description="Common Price SMAs: 10, 20, 50, 200 and Volume SMA: 20.",
    cores=0,
    ti=[
        {"kind": "sma", "length": 10},
        {"kind": "sma", "length": 20},
        {"kind": "sma", "length": 50},
        {"kind": "sma", "length": 200},
        {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOL"},
    ],
)

# Temporary Strategy DataClass Alias
Strategy = Study
AllStrategy = AllStudy
CommonStrategy = CommonStudy
