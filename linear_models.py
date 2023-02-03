import pandas as pd
from functions import remove_columns
from data_cleaning import important_amenities

df_madrid = pd.read_csv("airbnb_madrid_clean.csv")

##first we remove the columns that won't be used in the linear model
df_madrid = remove_columns(["ID", "Host ID", "Host Name", "Street", "Neighbourhood Cleansed", "City", "State",
"Zipcode", "Country", "Latitude", "Longitude", "Amenities Rating"], df_madrid)
df_madrid = remove_columns(important_amenities, df_madrid)

##then we make dummie variables for the categorical columns
print(df_madrid.info())
