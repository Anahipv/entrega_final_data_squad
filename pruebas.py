## creo que podemos convertir las funciones con map pero aun no deduzco bien la logica

def list_booleans(item, name_column, df):
    booleans = list(df[name_column].str.contains(item, case=False))
    return booleans

def create_column(df, item):
    dfcopy = df
    dfcopy[item] = False
    return df

def convert_column_map(list_column, name_column, df):
    map(lambda item : create_column(item, df), list_column)

from data_cleaning import important_features, df_madrid

print(convert_column_map(important_features, "Features", df_madrid))