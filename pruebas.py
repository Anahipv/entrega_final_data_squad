## creo que podemos convertir las funciones con map pero aun no deduzco bien la logica
# from data_cleaning import important_features, df_less_columns
import pandas as pd

def list_booleans(item, name_column, df):
    this_column = df[name_column].items()
    booleans = list(map(lambda x: item in x, this_column))
    return booleans

# print(list_booleans("TV", "Amenities", df_less_columns))


def create_column(df, item):
    dfcopy = df
    dfcopy[item] = False
    return df

def convert_column_map(list_column, name_column, df):
   df.map(create_column(df, list_column))

# print(convert_column_map(important_features, "Features", df_madrid))
