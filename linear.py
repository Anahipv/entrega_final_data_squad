import pandas as pd
from sklearn.model_selection import train_test_split

df_madrid = pd.read_csv('airbnb_madrid_clean.csv')

##train, test split
X = df_madrid.drop('Price', axis=1)
y = df_madrid['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)



