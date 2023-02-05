import pandas as pd
from functions import remove_columns
from data_cleaning import important_amenities
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df_madrid = pd.read_csv("airbnb_madrid_clean.csv")

##first we remove the columns that won't be used in the linear model
df_madrid = remove_columns(["Host ID", "Host Name", "Street", "Neighbourhood Cleansed", "City", "State", "Bed Type",
"Zipcode", "Country", "Latitude", "Longitude", "Amenities Rating", "Host Is Superhost", "Host Identity Verified",
"Review Scores Rating", "Host Response Rate"], df_madrid)
df_madrid = remove_columns(important_amenities, df_madrid)


##remove row with nan values in beds, bathroms and bedrooms
df_madrid = df_madrid.dropna(subset=["Beds", "Bathrooms", "Bedrooms"])

##we need to deal with nan values in security deposit and cleaning fee
##suggestion: median considering the number of rooms


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


total = X_train.isnull().sum().sort_values(ascending=False)
percent = (X_train.isnull().sum()/X_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head(20))


##this should work after removing Nans
#lr = LinearRegression()
#lr.fit(X_train, y_train)

##making predictions
#y_pred = lr.predict(X_test)

#_preds_df = pd.DataFrame(dict(observed=y_test, predicted=y_pred))
#_preds_df.head()

##evaluating the model
#print('Score: {}'.format(lr.score(X_test, y_test)))
#print('MSE: {}'.format(mean_squared_error(y_test, y_pred)))