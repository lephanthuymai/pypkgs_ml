from pypkgs_ml import __version__
from pypkgs_ml import pypkgs_ml as mypkg
import pandas as pd


def test_version():
    assert __version__ == "0.1.0"


def test_get_numeric_columns():
    df = pd.DataFrame({"c": [1], "a": [0]})
    cols = mypkg.get_numeric_columns(df)
    assert cols == ["c", "a"]
