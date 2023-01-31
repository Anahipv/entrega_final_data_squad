import pandas as pd
from functions import convert_column, remove_column

df = pd.read_csv("airbnb-listings.csv", sep=";")
rows, columns = df.shape

# print(f"We have {rows} rows and {columns} columns")

column_names = list(df)

# print(column_names)

columns_kept = ["ID", "Host ID", "Host Name", "Host Response Rate", "Street", 
"Neighbourhood Cleansed", "Neighbourhood Group Cleansed", "City", "State", "Zipcode", "Smart Location",
"Country", "Latitude", "Longitude", "Property Type", "Room Type", "Accommodates", "Bathrooms", "Bedrooms", 
"Beds", "Bed Type", "Amenities", "Price", "Security Deposit", "Cleaning Fee", "Guests Included",
"Number of Reviews", "Review Scores Rating", "Cancellation Policy", "Features"]

df_less_columns = df.filter(columns_kept, axis=1)

df_with_city = df_less_columns[df_less_columns.City.notnull()]

#remove airbnbs not in Madrid
df_madrid = df_with_city[df_with_city["City"].str.contains("Mad")]

# print(df_madrid.head())
# print(df_madrid.iloc[[1]])

amenities = set()
list_amenities = list(df_madrid["Amenities"])
for item in list_amenities:
    if type(item) == str:
        new_list = item.split(",")
        for amenity in new_list:
            amenities.add(amenity)

##remove shared rooms

important_features = ["Host Is Superhost", "Host Identity Verified"]

##internet and wireless should be combined in one column, maybe washer and dryer as well
important_amenities = ["Kitchen", "Internet", "Wireless", "Air conditioning", "Heating", "Washer", 
"Dryer", "Elevator", "Pets allowed", 'Wheelchair accessible', 'Smoking allowed', "TV", "Pool", 
'Pets live on this property', 'Free parking on premises',  'Lock on bedroom door', '24-hour check-in', 'Breakfast']

##cancelation policy should be numeric
cancelation_policy = {"strict": 0, "moderate": 1, "flexible": 2}

##maybe room type and property type should be numerical as well


##resetting indexes
df_madrid = df_madrid.reset_index()


##adding columns for important features and amenities
df_madrid = convert_column(important_features, "Features", df_madrid)

df_madrid = convert_column(important_amenities, "Amenities", df_madrid)

##removing the original columns for features and amenities
df_madrid = remove_column(["Features", "Amenities"], df_madrid)

df_madrid.to_csv("airbnb_madrid_clean")


