import pandas as pd
from functions import convert_column, remove_column

df = pd.read_csv("airbnb-listings.csv", sep=";")
rows, columns = df.shape

# print(f"We have {rows} rows and {columns} columns")

column_names = list(df)

# print(column_names)

columns_kept = ["ID", "Host ID", "Host Name", "Host Response Rate", "Street", 
"Neighbourhood Cleansed", "Neighbourhood Group Cleansed", "City", "State", "Zipcode",
"Country", "Latitude", "Longitude", "Property Type", "Room Type", "Accommodates", "Bathrooms", "Bedrooms", 
"Beds", "Bed Type", "Amenities", "Price", "Security Deposit", "Cleaning Fee", "Guests Included",
"Number of Reviews", "Review Scores Rating", "Cancellation Policy", "Features"]

df_less_columns = df.filter(columns_kept, axis=1)

df_with_city = df_less_columns[df_less_columns.City.notnull()]

#remove airbnbs not in Madrid
df_madrid = df_with_city[df_with_city["City"].str.contains("Mad", case=False)]


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

##property types
relevant_types = ["Apartment", "House"]
for index in range(len(df_madrid)):
    if df_madrid["Property Type"].iat[index] not in relevant_types:
        df_madrid["Property Type"].iat[index] = "Other"


##resetting indexes
df_madrid.reset_index(drop=True, inplace=True)

##adding columns for important features and amenities
df_madrid = convert_column(important_features, "Features", df_madrid)

df_madrid = convert_column(important_amenities, "Amenities", df_madrid)

##join columns "Internet" and "Wireless" under the internet column
for i in range(len(df_madrid)):
    df_madrid["Internet"].iat[i] = df_madrid["Internet"].iat[i] and df_madrid["Wireless"].iat[i]


##removing the original columns for Features, Amenities and Wireless
df_madrid = remove_column(["Features", "Amenities", "Wireless"], df_madrid)

important_amenities.remove("Wireless")

#cleaning column "Zipcode" 

print(df_madrid[['ID', "Neighbourhood Cleansed", "Neighbourhood Group Cleansed", "City", "State", "Zipcode"]]
        [(df_madrid['Zipcode'].isnull()) | (df_madrid['Zipcode'] == '-')])

df_madrid.loc[(df_madrid['Zipcode'].isnull()) | (df_madrid['Zipcode'] == '-'), 'Zipcode'] = ''

##convert the dataset to csv
df_madrid.to_csv("airbnb_madrid_clean.csv")

