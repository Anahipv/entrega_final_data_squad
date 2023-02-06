import matplotlib.pyplot as plt
import numpy as np

def create_and_populate_columns(list_columns, column_reference, df):
    for item in list_columns:
        df[item] = None
        booleans = list(df[column_reference].str.contains(item, case=False))
        for i in range(len(df)):
            df[item].iat[i] = booleans[i]
    return df

def remove_columns(list_columns, df):
    df = df.drop(columns = list_columns)
    return df

def change_nan_to_median(df, column_reference, column_change, index, median_dict):
    if np.isnan(df[column_change].iat[index]):
        key = df[column_reference].iat[index]
        median = median_dict[key]
        df[column_change].iat[index] = median

def create_median_dict(df, column_reference, column_median, list_keys):
    mydict = {}
    for key in list_keys:
        df_filtered = df[df[column_reference] == key]
        median = df_filtered[column_median].median()
        mydict[key] = median
    return mydict