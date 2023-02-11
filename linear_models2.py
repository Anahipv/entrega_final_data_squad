import pandas as pd
from functions import remove_columns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from transformers import DataFrameSelector
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.impute import SimpleImputer

df_madrid = pd.read_csv('airbnb_madrid_clean.csv')

##first we remove the columns that won't be used in the linear model
df_madrid = remove_columns(['Host ID', 'Host Name', 'Street', 'Neighbourhood Cleansed', 'City', 'State', 'Bed Type', "Amenities Rating", "Amenities Score",
'Country', 'Latitude', 'Longitude', 'ID', 'Number of Reviews', 'Host Identity Verified', 'Neighbourhood Group Cleansed'], df_madrid)


df_madrid.drop(df_madrid.columns[0], axis=1, inplace= True)


##now we divide in train and test
train, test = train_test_split(df_madrid, test_size=0.2, random_state=40)

train = train.dropna(subset=['Beds', 'Bathrooms', 'Bedrooms', 'Price', 'Review Scores Rating', 'Host Response Rate'])
test= test.dropna(subset=['Beds', 'Bathrooms', 'Bedrooms', 'Price', 'Review Scores Rating', 'Host Response Rate'])

##cleaning outliers
train = train[train['Bedrooms'] <= 5]
train = train[(train['Bathrooms'] >= 1) & (train['Bathrooms'] <= 3)]
train = train[train['Accommodates'] <= 8]
train = train[train['Guests Included'] <= 6]

##We obtained these values in the lists from the file graphs.py, analyzing the data with a boxplot
bedrooms_price = [(0,110), (1,125), (2,200), (3,280), (4,390), (5,500)]
bathrooms_price = [(1,140), (1.5,180), (2,270), (2.5,330), (3,450)]
accommodates_price = [(1,60), (2,100), (3,120), (4,140), (5,180), (6,210), (7,270), (8,300)]
guests_included_price = [(1, 125), (2, 135), (3, 150), (4,220), (5,230), (6,300)]

dict_columns = {'Bedrooms' : bedrooms_price, 'Bathrooms': bathrooms_price, 'Accommodates': accommodates_price, 
'Guests Included': guests_included_price}

for column_name in dict_columns.keys():
    list_prices = dict_columns[column_name]
    for i in range(len(list_prices)):
        train = train[(train[column_name] != list_prices[i][0]) | ((train[column_name] == list_prices[i][0]) & (train['Price'] <= list_prices[i][1] ))]

##spliting in Y (value that we want to predict) and X (variables that will be used in order to predict Y)
y_train = train['Price']
X_train = train.drop('Price', axis=1)
y_test = test['Price']
X_test = test.drop('Price', axis = 1)

print(f'"Partición de entrenamento"\n-----------------------\n{y_train.describe()}')

print(f'"Partición de test"\n-----------------------\n{y_test.describe()}')


##now we divide the column in numerical and categorica
numeric_columns = X_train.select_dtypes(include=['float64', 'int']).columns.to_list()
cat_columns = X_train.select_dtypes(include=['object', 'category']).columns.to_list()

##first we create a pipeline for the numerical columns
numeric_transformer = Pipeline(
                        steps=[
                            ('selector', DataFrameSelector(numeric_columns)),      
                            ('imputer', SimpleImputer(strategy="median")),
                            ('scaler', StandardScaler())
                        ]
                        )
                        
##then for the categorical
categorical_transformer = Pipeline(
                        steps= [
                            ('selector', DataFrameSelector(cat_columns)),
                            ('onehot', OneHotEncoder(sparse=False, handle_unknown='ignore'))
                        ]
                        )

##then we combine the two using FeatureUnion
preprocessor =  FeatureUnion(
                transformer_list = [
                    ('numeric', numeric_transformer),
                    ('cat', categorical_transformer)
                ]
                )

X_train_prepared = preprocessor.fit_transform(X_train)
X_test_prepared = preprocessor.transform(X_test)


lr = RidgeCV(alphas=(0.1, 1.0, 6.6, 10.0))
lr.fit(X_train_prepared, y_train)


##making predictions
y_pred = lr.predict(X_test_prepared)

_preds_df = pd.DataFrame(dict(observed=y_test, predicted=y_pred))
_preds_df.head()

##evaluating the model
print('MSE: {}'.format(mean_squared_error(y_test, y_pred)))
print('Mean Percentual Error: {}'.format(mean_absolute_percentage_error(y_test, y_pred)))


##random forest for comparison
rf = RandomForestRegressor()
rf.fit(X_train_prepared, y_train)

y_pred_rd = rf.predict(X_test_prepared)

print('Mean Percentual Error (RF): {}'.format(mean_absolute_percentage_error(y_test, y_pred_rd)))