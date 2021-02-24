import pandas as pd


def get_numeric_columns(df, drop_columns=[]):
    """return the list of numeric columns' names

    Args:
        df (DataFrame): a data frame
        drop_columns (array of strings): a list of column names to ignore

    Returns:
        list: list of numeric column names

    Examples:
        from pypkgs_ml import pypkgs_ml as mypkg
        import pandas as pd
        df = pd.DataFrame({'c'=[1], 'a'=[0]})
        cols = mypkg.get_numeric_columns(df)
    """
    return df.select_dtypes("number").drop(columns=drop_columns).columns.tolist()
