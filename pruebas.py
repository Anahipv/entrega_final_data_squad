def create_and_populate_columns(list_column, column_reference, df):
    for item in list_column:
        df[item] = list(df[column_reference].str.contains(item, case=False))
    return df

def create_column(df, column):
    df[column] = None
    return df

def column_contains(df, column_reference, item):
    booleans = list(df[column_reference].str.contains(item, case=False))
    return booleans

def populate_column_with_list(df, column, list_data):
    for i in range(len(df)):
        df[column].iat[i] = list_data[i]
    return df

def create_and_populate_columns2(list_column, column_reference, df):
    for column in list_column:
        df = create_column(df, column)
        booleans = column_contains(df, column_reference, column)
        df = populate_column_with_list(df, column, booleans)
    return df

    