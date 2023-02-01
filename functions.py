import matplotlib.pyplot as plt

def convert_column(list_column, name_column, df):
    for item in list_column:
        df[item] = False
        booleans = list(df[name_column].str.contains(item, case=False))
        for i in range(len(df)):
            df[item].iat[i] = booleans[i]
    return df

def remove_column(list_columns, df):
    df = df.drop(columns = list_columns)
    return df

