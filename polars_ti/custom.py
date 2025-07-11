# -*- coding: utf-8 -*-
import importlib
import os
import sys
import types
from glob import glob
from os.path import abspath, basename, exists, join, splitext

import polars_ti
from polars_ti._typing import DictLike


def bind(name: str, f: types.FunctionType, method: types.MethodType = None):
    """
    Helper function to bind the function and class method defined in a custom
    indicator module to the active polars_ti instance.

    Args:
        function_name (str): The name of the indicator within polars_ti
        function (fcn): The indicator function
        method (fcn): The class method corresponding to the passed function
    """
    setattr(polars_ti, name, f)
    setattr(polars_ti.TechnicalIndicators, name, method)


def create_dir(path: str, create_categories: bool = True, verbose: bool = True):
    """
    Helper function to setup a suitable folder structure for working with
    custom indicators. You only need to call this once whenever you want to
    setup a new custom indicators folder.

    Args:
        path (str): Full path to where you want your indicator tree
        create_categories (bool): If True create category sub-folders
        verbose (bool): If True print verbose output of results
    """

    # ensure that the passed directory exists / is readable
    if not exists(path):
        os.makedirs(path)
        if verbose:
            print(f"[i] Created main directory '{path}'.")

    # list the contents of the directory
    # dirs = glob(abspath(join(path, '*')))

    # optionally add any missing category subdirectories
    if create_categories:
        for sd in [*polars_ti.Category]:
            d = abspath(join(path, sd))
            if not exists(d):
                os.makedirs(d)
                if verbose:
                    dirname = basename(d)
                    print(f"[i] Created an empty sub-directory '{dirname}'.")


def get_module_functions(module: types.ModuleType) -> DictLike:
    """
     Helper function to get the functions of an imported module
     as a dictionary.

    Args:
        module: python module

    Returns:
        dict: module functions mapping
        {
            "func1_name": func1,
            "func2_name": func2,...
        }
    """
    module_functions = {}

    for name, item in vars(module).items():
        if isinstance(item, types.FunctionType):
            module_functions[name] = item

    return module_functions


def import_dir(path: str, verbose: bool = True):
    """
    Import a directory of custom indicators into polars_ti

    Args:
        path (str): Full path to your indicator tree
        verbose (bool): If True verbose output of results

    This method allows you to experiment and develop your own technical
    indicators in a separate local directory of your choice but
    use them seamlessly together with the existing polars_ti functions just
    like if they were part of polars_ti.

    If you at some late point would like to push them into the polars_ti
    library you can do so very easily by following the step by step
    instruction here https://github.com/CMobley7/polars-ti/issues/355.

    A brief example of usage:

    1. Loading the 'ti' module:
    >>> import pandas as pd
    >>> import polars_ti as ti

    2. Create an empty directory on your machine where you want to work with
    your indicators. Invoke polars_ti.custom.import_dir once to pre-populate
    it with sub-folders for all available indicator categories, e.g.:

    >>> import os
    >>> from os.path import abspath, join, expanduser
    >>> from polars_ti.custom import create_dir, import_dir
    >>> ti_dir = abspath(join(expanduser("~"), "my_indicators"))
    >>> create_dir(ti_dir)

    3. You can now create your own custom indicator e.g. by copying existing
    ones from polars_ti core module and modifying them.

    IMPORTANT: Each custom indicator should have a unique name and have both
    a) a function named exactly as the module, e.g. 'ni' if the module is ni.py
    b) a matching method used by TechnicalIndicators named as the module but
    ending with '_method'. E.g. 'ni_method'

    In essence these modules should look exactly like the standard indicators
    available in categories under the polars_ti-folder. The only difference
    will be an addition of a matching class method.

    For an example of the correct structure, look at the example ni.py in the
    examples folder.

    The ni.py indicator is a trend indicator so therefore we drop it into the
    sub-folder named trend. Thus we have a folder structure like this:

    ~/my_indicators/
    │
    ├── candles/
    .
    .
    └── trend/
    .      └── ni.py
    .
    └── volume/

    4. We can now dynamically load all our custom indicators located in our
    designated indicators directory like this:

    >>> import_dir(ti_dir)

    If your custom indicator(s) loaded successfully then it should behave exactly
    like all other native indicators in polars_ti, including help functions.
    """
    # ensure that the passed directory exists / is readable
    if not exists(path):
        print(f"[X] Unable to read the directory '{path}'.")
        return

    # list the contents of the directory
    dirs = glob(abspath(join(path, "*")))

    # traverse full directory, importing all modules found there
    for d in dirs:
        dirname = basename(d)

        # only look in directories which are valid polars_ti categories
        if dirname not in [*polars_ti.Category]:
            if verbose and dirname not in ["__pycache__", "__init__.py"]:
                print(
                    f"[i] Skipping the sub-directory '{dirname}' since it's not a valid polars_ti category."
                )
            continue

        # for each module found in that category (directory)...
        for module in glob(abspath(join(path, dirname, "*.py"))):
            module_name = splitext(basename(module))[0]
            if module_name not in ["__init__"]:
                # ensure that the supplied path is included in our python path
                if d not in sys.path:
                    sys.path.append(d)

                # (re)load the indicator module
                module_functions = load_indicator_module(module_name)

                # figure out which of the modules functions to bind to polars_ti
                _callable = module_functions.get(module_name, None)
                _method_callable = module_functions.get(f"{module_name}_method", None)

                if _callable == None:
                    print(
                        f"[X] Unable to find a function named '{module_name}' in the module '{module_name}.py'."
                    )
                    continue
                if _method_callable == None:
                    missing_method = f"{module_name}_method"
                    print(
                        f"[X] Unable to find a method function named '{missing_method}' in the module '{module_name}.py'."
                    )
                    continue

                # add it to the correct category if it's not there yet
                if module_name not in polars_ti.Category[dirname]:
                    polars_ti.Category[dirname].append(module_name)

                bind(module_name, _callable, _method_callable)
                if verbose:
                    print(
                        f"[i] Successfully imported the custom indicator '{module}' into category '{dirname}'."
                    )


def load_indicator_module(name: str) -> dict:
    """
     Helper function to (re)load an indicator module.

    Returns:
        dict: module functions mapping
        {
            "func1_name": func1,
            "func2_name": func2,...
        }

    """
    try:
        module = importlib.import_module(name)
    except Exception as ex:
        print(f"[X] An error occurred when attempting to load module {name}: {ex}")
        sys.exit(1)

    # reload to refresh previously loaded module
    module = importlib.reload(module)
    return get_module_functions(module)
