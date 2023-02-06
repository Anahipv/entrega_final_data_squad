import pandas as pd
from functions import remove_columns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

df_madrid = pd.read_csv("airbnb_madrid_clean.csv")

important_amenities = ["Kitchen", "Internet", "Air conditioning", "Heating", "Washer", 
"Dryer", "Elevator", 'Wheelchair accessible', "TV", "Pool", '24-hour check-in']

print(df_madrid["Room Type"].unique())
##first we remove the columns that won't be used in the linear model
df_madrid = remove_columns(["Host ID", "Host Name", "Street", "Neighbourhood Cleansed", "City", "State", "Bed Type",
"Zipcode", "Country", "Latitude", "Longitude", "Amenities Rating", "Host Is Superhost", "Host Identity Verified",
"Review Scores Rating", "Host Response Rate", "ID"], df_madrid)
df_madrid = remove_columns(important_amenities, df_madrid)



##remove row with nan values in beds, bathroms and bedrooms
df_madrid = df_madrid.dropna(subset=["Beds", "Bathrooms", "Bedrooms", "Price"])

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


for index in range(len(df_madrid)):
    if np.isnan(df_madrid["Security Deposit"].iat[index]):
        number_rooms = df_madrid["Bedrooms"].iat[index]
        median_sd = dict_sd[number_rooms]
        df_madrid["Security Deposit"].iat[index] = median_sd
    if np.isnan(df_madrid["Cleaning Fee"].iat[index]):
        number_rooms = df_madrid["Bedrooms"].iat[index]
        median_cf = dict_cf[number_rooms]
        df_madrid["Cleaning Fee"].iat[index] = median_cf


##then we make dummie variables for the categorical columns
cat_columns = ["Neighbourhood Group Cleansed", "Property Type", "Room Type", "Cancellation Policy"]

for col in cat_columns:
    one_hot = pd.get_dummies(df_madrid[col])
    df_madrid = df_madrid.drop(col, axis=1)
    df_madrid = df_madrid.join(one_hot)


##train, test split
target = df_madrid["Price"]
predictors = df_madrid.drop(columns = ["Price"])
X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.3, random_state=40)


total = df_madrid.isnull().sum().sort_values(ascending=False)
percent = (df_madrid.isnull().sum()/df_madrid.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head(20))


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