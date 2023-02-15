
def create_and_populate_columns(list_columns, column_reference, df):
    '''
    Creates columns from list_columns and populates them with booleans if the new column exists in column_refence
    '''
    for item in list_columns:
        df[item] = None
        booleans = list(df[column_reference].str.contains(item, case=False))
        df[item] = booleans
    return df

def remove_columns(list_columns, df):
    '''
    Removes all the columns in the list_columns
    '''
    df = df.drop(columns = list_columns)
    return df


