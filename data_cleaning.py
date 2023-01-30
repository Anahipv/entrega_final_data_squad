import pandas as pd

df = pd.read_csv("airbnb-listings.csv", sep=";")
rows, columns = df.shape

print(f"We have {rows} rows and {columns} columns")

column_names = list(df)

print(column_names)

columns_kept = ["ID", "Host ID", "Host Name", "Host Response Rate", "Street", 
"Neighbourhood Cleansed", "Neighbourhood Group Cleansed", "City", "State", "Zipcode", "Smart Location",
"Country", "Latitude", "Longitude", "Property Type", "Room Type", "Accommodates", "Bathrooms", "Bedrooms", 
"Beds", "Bed Type", "Amenities", "Price", "Security Deposit", "Cleaning Fee", "Guests Included",
"Number of Reviews", "Review Scores Rating", "Cancellation Policy", "Features"]

df_less_columns = df.filter(columns_kept, axis=1)

df_with_city = df_less_columns[df_less_columns.City.notnull()]

#remove airbnbs not in Madrid
df_madrid = df_with_city[df_with_city["City"].str.contains("Mad")]

##remove shared rooms

important_features = ["Host Is SuperHost", "Host Identity Verified"]

##internet and wireless should be combined in one column, maybe washer and dryer as well
important_amenities = ["Kitchen", "Internet", "Wireless", "Air conditioning", "Heating", "Washer", "Dryer", "Elevator"]

##cancelation policy should be numeric
cancelation_policy = {"strict": 0, "moderate": 1, "flexible": 2}

##maybe room type and property type should be numerical as well


##adding columns for important features
for feature in important_features:
    df_madrid[feature] = df_madrid.loc[df_madrid["Features"].str.contains(feature)]