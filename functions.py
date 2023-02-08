import matplotlib.pyplot as plt
import numpy as np

def create_and_populate_columns(list_columns, column_reference, df):
    '''
    Creates columns from list_columns and populates them with booleans if the new column exists in column_refence
    '''
    for item in list_columns:
        df[item] = list(df[column_reference].str.contains(item, case=False))
    return df

def remove_columns(list_columns, df):
    '''
    Removes all the columns in the list_columns
    '''
    df = df.drop(columns = list_columns)
    return df

def change_nan_to_median(df, column_reference, column_change, index, median_dict):
    '''
    Changes the value in the row if the value is a Nan in the column_change.
    Needs a column_reference where look the median in the dicttionary.
    '''
    if np.isnan(df[column_change].iat[index]):
        key = df[column_reference].iat[index]
        median = median_dict[key]
        df[column_change].iat[index] = median


def create_median_dict(df, column_reference, column_median, list_keys):
    '''
    Creates a dicctionary where keys exists in the column_reference like a value, and the value is a median.
    For each key in the list_keys:
        first filteres the dataframe where the column_reference is equal to the key,
        then calculates the median for de dataframe filtered and creates the dicctionary woth the key and the median
    '''
    mydict = {}
    for key in list_keys:
        df_filtered = df[df[column_reference] == key]
        median = df_filtered[column_median].median()
        mydict[key] = median
    return mydict