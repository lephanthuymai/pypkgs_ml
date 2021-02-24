import pandas as pd


def get_numeric_columns(df, drop_columns=[]):
    """return the list of numeric columns' names

    Args:
        df (DataFrame): a data frame
        drop_columns (array of strings): a list of column names to ignore

    Returns:
        list: list of numeric column names
    """
    return df.select_dtypes("number").drop(columns=drop_columns).columns.tolist()
