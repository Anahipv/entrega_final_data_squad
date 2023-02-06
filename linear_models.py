import pandas as pd
from functions import remove_columns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

df_madrid = pd.read_csv("airbnb_madrid_clean.csv")

important_amenities = ["Kitchen", "Internet", "Air conditioning", "Heating", "Washer", 
"Dryer", "Elevator", 'Wheelchair accessible', "TV", "Pool", '24-hour check-in']

##first we remove the columns that won't be used in the linear model and the rows where Room Type is Shared room

df_madrid = df_madrid[df_madrid['Room Type'] != 'Shared room']

df_madrid = remove_columns(["Host ID", "Host Name", "Street", "Neighbourhood Cleansed", "City", "State", "Bed Type",
"Zipcode", "Country", "Latitude", "Longitude", "Host Is Superhost", "Host Identity Verified",
"Review Scores Rating", "Host Response Rate", "ID", "Guests Included","Number of Reviews"], df_madrid)
df_madrid = remove_columns(important_amenities, df_madrid)
df_madrid.drop(df_madrid.columns[0], axis=1, inplace= True)


##remove row with nan values in beds, bathroms and bedrooms
df_madrid = df_madrid.dropna(subset=["Beds", "Bathrooms", "Bedrooms", "Price"])

print('CORRELACION ORIGINAL')
print(df_madrid.corr()['Price'])

##we need to deal with nan values in security deposit and cleaning fee
##we will use the median considering the number of rooms
dict_sd = {}
dict_cf = {}
number_of_rooms = df_madrid["Bedrooms"].unique()
for number in number_of_rooms:
    df_filtered = df_madrid[df_madrid["Bedrooms"] == number]
    median_sd = df_filtered["Security Deposit"].median()
    dict_sd[number] = median_sd
    median_cf = df_filtered["Cleaning Fee"].median()
    dict_cf[number] = median_cf

print(f'Median of "Security Deposit" per Bedrooms: {dict_sd}')
print(f'Median of "Cleaning Fee" per Bedrooms: {dict_cf}')


##we created two new columns to find out if the data previously existed in 'Security Deposit' and 'Cleaning Fee'
df_madrid['SD Exists'] = 1
df_madrid['CF Exists'] = 1

for index in range(len(df_madrid)):
    if np.isnan(df_madrid["Security Deposit"].iat[index]):
        number_rooms = df_madrid["Bedrooms"].iat[index]
        median_sd = dict_sd[number_rooms]
        df_madrid["Security Deposit"].iat[index] = median_sd
        df_madrid['SD Exists'].iat[index] = 0
    if np.isnan(df_madrid["Cleaning Fee"].iat[index]):
        number_rooms = df_madrid["Bedrooms"].iat[index]
        median_cf = dict_cf[number_rooms]
        df_madrid["Cleaning Fee"].iat[index] = median_cf
        df_madrid['CF Exists'].iat[index] = 0

##cleaning outliers
df_madrid = df_madrid[df_madrid['Bedrooms'] <= 5]
df_madrid = df_madrid[(df_madrid['Bathrooms'] >= 1) & (df_madrid['Bathrooms'] <= 3)]
df_madrid = df_madrid[df_madrid['Accommodates'] <= 8]

##We obtained these values in the lists from the file graphs.py, analyzing the data with a boxplot
bedrooms_price = [(0,110), (1,125), (2,200), (3,280), (4,390), (5,500)]
bathrooms_price = [(1,140), (1.5,180), (2,270), (2.5,330), (3,450)]
accommodates_price = [(1,60), (2,100), (3,120), (4,140), (5,180), (6,210), (7,270), (8,300)]
amenities_rating_price = [('C',150), ('B',200), ('A',300)]

for i in range(6):
    if i == 0:
        df_madrid = df_madrid[(df_madrid['Bedrooms'] > 0) | ((df_madrid["Bedrooms"] == 0) & (df_madrid["Price"] <= bedrooms_price[0] ))]
    else:
        df_madrid = df_madrid[(df_madrid['Bedrooms'] != i) | ((df_madrid["Bedrooms"] == i) & (df_madrid["Price"] <= bedrooms_price[i] ))]

df_madrid = df_madrid[(df_madrid['Bathrooms'] != 1) | ((df_madrid["Bathrooms"] == 1) & (df_madrid["Price"] <= 140 ))]
df_madrid = df_madrid[(df_madrid['Bathrooms'] != 1.5) | ((df_madrid["Bathrooms"] == 1.5) & (df_madrid["Price"] <= 180 ))]
df_madrid = df_madrid[(df_madrid['Bathrooms'] != 2) | ((df_madrid["Bathrooms"] == 2) & (df_madrid["Price"] <= 270 ))]
df_madrid = df_madrid[(df_madrid['Bathrooms'] != 2.5) | ((df_madrid["Bathrooms"] == 2.5) & (df_madrid["Price"] <= 330 ))]
df_madrid = df_madrid[(df_madrid['Bathrooms'] != 3) | ((df_madrid["Bathrooms"] == 3) & (df_madrid["Price"] <= 450 ))]

df_madrid = df_madrid[(df_madrid['Accommodates'] != 1) | ((df_madrid["Accommodates"] == 1) & (df_madrid["Price"] <= 60 ))]
df_madrid = df_madrid[(df_madrid['Accommodates'] != 2) | ((df_madrid["Accommodates"] == 2) & (df_madrid["Price"] <= 100 ))]
df_madrid = df_madrid[(df_madrid['Accommodates'] != 3) | ((df_madrid["Accommodates"] == 3) & (df_madrid["Price"] <= 120 ))]
df_madrid = df_madrid[(df_madrid['Accommodates'] != 4) | ((df_madrid["Accommodates"] == 4) & (df_madrid["Price"] <= 140 ))]
df_madrid = df_madrid[(df_madrid['Accommodates'] != 5) | ((df_madrid["Accommodates"] == 5) & (df_madrid["Price"] <= 180 ))]
df_madrid = df_madrid[(df_madrid['Accommodates'] != 6) | ((df_madrid["Accommodates"] == 6) & (df_madrid["Price"] <= 210 ))]
df_madrid = df_madrid[(df_madrid['Accommodates'] != 7) | ((df_madrid["Accommodates"] == 7) & (df_madrid["Price"] <= 270 ))]
df_madrid = df_madrid[(df_madrid['Accommodates'] != 8) | ((df_madrid["Accommodates"] == 8) & (df_madrid["Price"] <= 300 ))]

df_madrid = df_madrid[(df_madrid['Amenities Rating'] != 'C') | ((df_madrid["Amenities Rating"] == 'C') & (df_madrid["Price"] <= 150 ))]
df_madrid = df_madrid[(df_madrid['Amenities Rating'] != 'B') | ((df_madrid["Amenities Rating"] == 'B') & (df_madrid["Price"] <= 200 ))]
df_madrid = df_madrid[(df_madrid['Amenities Rating'] != 'A') | ((df_madrid["Amenities Rating"] == 'A') & (df_madrid["Price"] <= 300 ))]

print(df_madrid)

df_madrid.drop('Amenities Rating', axis=1, inplace= True)

print('CORRELACION MODIFICADA con OUTLIERS')
print(df_madrid.corr()['Price'])


##then we make dummie variables for the categorical columns
cat_columns = ["Neighbourhood Group Cleansed", "Property Type", "Room Type", "Cancellation Policy",]

for col in cat_columns:
    one_hot = pd.get_dummies(df_madrid[col])
    df_madrid = df_madrid.drop(col, axis=1)
    df_madrid = df_madrid.join(one_hot)

print('CORRELACION MODIFICADA con ONE-HOT')
print(df_madrid.corr()['Price'])

##train, test split
target = df_madrid["Price"]
predictors = df_madrid.drop(columns = ["Price"])
X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.3, random_state=40)


total = df_madrid.isnull().sum().sort_values(ascending=False)
percent = (df_madrid.isnull().sum()/df_madrid.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])


##this should work after removing Nans
lr = LinearRegression()
lr.fit(X_train, y_train)


##making predictions
y_pred = lr.predict(X_test)

_preds_df = pd.DataFrame(dict(observed=y_test, predicted=y_pred))
_preds_df.head()

##evaluating the model
print('Score: {}'.format(lr.score(X_test, y_test)))
print('MSE: {}'.format(mean_squared_error(y_test, y_pred)))