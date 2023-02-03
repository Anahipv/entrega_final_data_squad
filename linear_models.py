import pandas as pd
from functions import remove_columns
from data_cleaning import important_amenities

df_madrid = pd.read_csv("airbnb_madrid_clean.csv")

##first we remove the columns that won't be used in the linear model
df_madrid = remove_columns(["Host ID", "Host Name", "Street", "Neighbourhood Cleansed", "City", "State",
"Zipcode", "Country", "Latitude", "Longitude", "Amenities Rating", "Host Is Superhost", "Host Identity Verified"], df_madrid)
df_madrid = remove_columns(important_amenities, df_madrid)

##then we make dummie variables for the categorical columns
cat_columns = ["Neighbourhood Group Cleansed", "Property Type", "Room Type", "Cancellation Policy"]

for col in cat_columns:
    one_hot = pd.get_dummies(df_madrid[col])
    df_madrid = df_madrid.drop(col, axis=1)
    df_madrid = df_madrid.join(one_hot)
    
print(df_madrid.info())
