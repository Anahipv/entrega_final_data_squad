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

#df_madrid = df_madrid[df_madrid['Room Type'] != 'Shared room']

df_madrid = remove_columns(["Host ID", "Host Name", "Street", "Neighbourhood Cleansed", "City", "State", "Bed Type",
"Zipcode", "Country", "Latitude", "Longitude", "Host Is Superhost", "Host Identity Verified",
"Review Scores Rating", "Host Response Rate", "ID", "Guests Included","Number of Reviews"], df_madrid)
df_madrid = remove_columns(important_amenities, df_madrid)
df_madrid.drop(df_madrid.columns[0], axis=1, inplace= True)

##then we make dummie variables for the categorical columns
cat_columns = ["Neighbourhood Group Cleansed", "Property Type", "Room Type", "Cancellation Policy",]

for col in cat_columns:
    one_hot = pd.get_dummies(df_madrid[col])
    df_madrid = df_madrid.drop(col, axis=1)
    df_madrid = df_madrid.join(one_hot)


##now we divide in train and test
#target = df_madrid["Price"]
#predictors = df_madrid.drop(columns = ["Price"])
train, test = train_test_split(df_madrid, test_size=0.2, random_state=40)


##now we will deal with missing values and outliers in the train set
##first we remove the rows with nan values in beds, bathroms, bedrooms and price
train = train.dropna(subset=["Beds", "Bathrooms", "Bedrooms", "Price"])

#print('CORRELACION ORIGINAL')
#print(train.corr()['Price'])

##we need to deal with nan values in security deposit and cleaning fee
##we will use the median considering the number of rooms
dict_sd = {}
dict_cf = {}
number_of_rooms = train["Bedrooms"].unique()
for number in number_of_rooms:
    df_filtered = train[train["Bedrooms"] == number]
    median_sd = df_filtered["Security Deposit"].median()
    dict_sd[number] = median_sd
    median_cf = df_filtered["Cleaning Fee"].median()
    dict_cf[number] = median_cf

#print(f'Median of "Security Deposit" per Bedrooms: {dict_sd}')
#print(f'Median of "Cleaning Fee" per Bedrooms: {dict_cf}')


for index in range(len(train)):
    if np.isnan(train["Security Deposit"].iat[index]):
        number_rooms = train["Bedrooms"].iat[index]
        median_sd = dict_sd[number_rooms]
        train["Security Deposit"].iat[index] = median_sd
    if np.isnan(train["Cleaning Fee"].iat[index]):
        number_rooms = train["Bedrooms"].iat[index]
        median_cf = dict_cf[number_rooms]
        train["Cleaning Fee"].iat[index] = median_cf

##cleaning outliers
train = train[train['Bedrooms'] <= 5]
train = train[(train['Bathrooms'] >= 1) & (train['Bathrooms'] <= 3)]
train = train[train['Accommodates'] <= 8]

##We obtained these values in the lists from the file graphs.py, analyzing the data with a boxplot
bedrooms_price = [(0,110), (1,125), (2,200), (3,280), (4,390), (5,500)]
bathrooms_price = [(1,140), (1.5,180), (2,270), (2.5,330), (3,450)]
accommodates_price = [(1,60), (2,100), (3,120), (4,140), (5,180), (6,210), (7,270), (8,300)]
amenities_rating_price = [('C',150), ('B',200), ('A',300)]

dict_columns = {"Bedrooms" : bedrooms_price, "Bathrooms": bathrooms_price, "Accommodates": accommodates_price, "Amenities Rating": amenities_rating_price}

for column_name in dict_columns.keys():
    list_prices = dict_columns[column_name]
    for i in range(len(list_prices)):
        train = train[(train[column_name] != list_prices[i][0]) | ((train[column_name] == list_prices[i][0]) & (train["Price"] <= list_prices[i][1] ))]


##now that we've used the columns Amenities Rating to remove outliers, we will drop it
##we won't convert it using one hot encoding because Amenities Scores exists
train.drop("Amenities Rating", axis=1, inplace= True)
test.drop("Amenities Rating", axis=1, inplace= True)
#print(train)


#print('CORRELACION MODIFICADA con OUTLIERS')
#print(train.corr()['Price'])


#print('CORRELACION MODIFICADA con ONE-HOT')
#print(train.corr()['Price'])


total = train.isnull().sum().sort_values(ascending=False)
percent = (train.isnull().sum()/train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])


#now we deal with the nans in the test (if we have the time, make it into a pipeline)
##first we remove the rows with nan values in beds, bathroms, bedrooms and price
test = test.dropna(subset=["Beds", "Bathrooms", "Bedrooms", "Price"])

##we need to deal with nan values in security deposit and cleaning fee
##we will use the median from train considering the number of rooms
for index in range(len(test)):
    if np.isnan(test["Security Deposit"].iat[index]):
        number_rooms = test["Bedrooms"].iat[index]
        median_sd = dict_sd[number_rooms]
        test["Security Deposit"].iat[index] = median_sd
    if np.isnan(test["Cleaning Fee"].iat[index]):
        number_rooms = test["Bedrooms"].iat[index]
        median_cf = dict_cf[number_rooms]
        test["Cleaning Fee"].iat[index] = median_cf


y_train = train["Price"]
X_train = train.drop("Price", axis=1)
y_test = test["Price"]
X_test = test.drop("Price", axis = 1)


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