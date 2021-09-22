import pandas as pd
import numpy as np



def merge_cols(df, col1, col2, col_out):

    sf = df[[col1, col2]]
    missing = df.index[sf.apply(np.isnan).all(axis=1)] # boolean series (True -> both values missing, False -> at least one value defined)
    assert all(sf.apply(np.isnan).sum(axis=1)>=1), 'Error: only one ID can have a value!' # will throw an error when both columns contain a value

    df[col_out] = sf.sum(axis=1)
    df[col_out][missing] = None
    return df

