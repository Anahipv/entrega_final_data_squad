import pandas as pd
from functions import create_and_populate_columns, remove_columns

df = pd.read_csv('airbnb-listings.csv', sep=';')
rows, columns = df.shape

print(f'We have {rows} rows and {columns} columns')

column_names = list(df)

print(column_names)

columns_kept = ['ID', 'Host ID', 'Host Name', 'Host Response Rate', 'Street', 
'Neighbourhood Cleansed', 'Neighbourhood Group Cleansed', 'City', 'State', 'Zipcode',
'Country', 'Latitude', 'Longitude', 'Property Type', 'Room Type', 'Accommodates', 'Bathrooms', 'Bedrooms', 
'Beds', 'Bed Type', 'Amenities', 'Price', 'Security Deposit', 'Cleaning Fee', 'Guests Included',
'Number of Reviews', 'Review Scores Rating', 'Cancellation Policy', 'Features']


df_less_columns = df.filter(columns_kept, axis=1)

df_with_city = df_less_columns[df_less_columns.City.notnull()]

#remove airbnbs not in Madrid
df_madrid = df_with_city[df_with_city['City'].str.contains('Mad', case=False)]


amenities = set()
list_amenities = list(df_madrid['Amenities'])
for item in list_amenities:
    if type(item) == str:
        new_list = item.split(',')
        for amenity in new_list:
            amenities.add(amenity)

important_features = ['Host Is Superhost', 'Host Identity Verified']
important_amenities = ['Kitchen', 'Internet', 'Wireless', 'Air conditioning', 'Heating', 'Washer', 
'Dryer', 'Elevator', 'Wheelchair accessible', 'TV', 'Pool', '24-hour check-in']

##we group the data in property types like apartment, house or other
relevant_types = ['Apartment', 'House']
for index in range(len(df_madrid)):
    if df_madrid['Property Type'].iat[index] not in relevant_types:
        df_madrid['Property Type'].iat[index] = 'Other'


##resetting indexes
df_madrid.reset_index(drop=True, inplace=True)


##adding columns for important features and amenities
df_madrid = create_and_populate_columns(important_features, 'Features', df_madrid)

df_madrid = create_and_populate_columns(important_amenities, 'Amenities', df_madrid)


##join columns 'Internet' and 'Wireless' under the internet column
for i in range(len(df_madrid)):
    df_madrid['Internet'].iat[i] = df_madrid['Internet'].iat[i] and df_madrid['Wireless'].iat[i]


##removing the original columns for Features, Amenities and Wireless
df_madrid = remove_columns(['Features', 'Amenities', 'Wireless'], df_madrid)

important_amenities.remove('Wireless')

#cleaning column 'Zipcode' 
df_madrid.loc[(df_madrid['Zipcode'].isnull()) | (df_madrid['Zipcode'] == '-'), 'Zipcode'] = ''

df_madrid_copy  = df_madrid[['Price', 'Accommodates', 'Bathrooms', 'Bedrooms', 'Beds', 'Cleaning Fee', 'Security Deposit',
                            'Kitchen', 'Internet', 'Air conditioning', 'Heating', 'Washer', 'Dryer', 'Elevator', 'Wheelchair accessible', 
                            'TV', 'Pool', '24-hour check-in']]


##we will create a new 'Amenities Score' column. The data will be obtained by adding the weight in the correlation for each amenity in the row
corr = df_madrid_copy.corr(numeric_only=False)

dict_weights = {}
print(corr["Price"])
for amenity in important_amenities:
    weight = corr['Price'][amenity]
    dict_weights[amenity] = weight

scores = []
for index in range(len(df_madrid)):
    score = 0
    for amenity in important_amenities:
        if df_madrid[amenity].iat[index]:
            score += dict_weights[amenity]
    scores.append(score)

df_madrid['Amenities Score'] = scores


##based in the amenities score's quantiles, we create a new classification in the scale 'A', 'B', 'C'
q3 = df_madrid['Amenities Score'].quantile(0.33)
q6 = df_madrid['Amenities Score'].quantile(0.67)

ratings = []
for index in range(len(df_madrid)):
    if df_madrid['Amenities Score'].iat[index] < q3:
        ratings.append('C')
    elif df_madrid['Amenities Score'].iat[index] < q6:
        ratings.append('B')
    else:
        ratings.append('A')
df_madrid['Amenities Rating'] = ratings


#convert the dataset to csv
df_madrid.to_csv('airbnb_madrid_clean.csv')
