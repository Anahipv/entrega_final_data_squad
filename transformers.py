from sklearn.base import TransformerMixin
import pandas as pd
from functions import remove_columns, change_nan_to_median
from sklearn.preprocessing import OneHotEncoder

class DropNans(TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y):
        self.X = X
        self.y = y
        return self

    def transform(self, X, y):
        # drop incomplete rows
        columns = ['Beds', 'Bathrooms', 'Bedrooms', 'Price', 'Review Scores Rating', 'Host Response Rate']
        Xp = pd.DataFrame(X)
        Yp = pd.DataFrame(y)
        data = Xp.join(Yp)
        datadrop = data.dropna(subset=columns).to_numpy()
        Ydrop = datadrop['Price']
        Xdrop = datadrop.drop('Price', axis = 1)
        return Xdrop, Ydrop

class DropAmenities(TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None):
        self.X = X
        return self

    def transform(self, X, y=None):
        # drop incomplete rows
        Xp = pd.DataFrame(X)
        Xdrop = Xp.drop('Amenities Rating', axis=1, inplace= True).to_numpy()
        return Xdrop

class RemoveColumns(TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None):
        self.X = X
        return self

    def transform(self, X, y=None):
        #remove the selected columns
        columns_list = ['Host ID', 'Host Name', 'Street', 'Neighbourhood Cleansed', 'City', 'State', 'Bed Type', "Amenities Rating",
'Country', 'Latitude', 'Longitude', 'ID', 'Number of Reviews', 'Host Identity Verified', 'Neighbourhood Group Cleansed']
        Xp = pd.DataFrame(X)
        Xdrop = remove_columns(columns_list, Xp).to_numpy()
        return Xdrop

class HostNumerical(TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None):
        self.X = X
        return self

    def transform(self, X, y=None):
        Xp = pd.DataFrame(X)
        for index in range(len(Xp)):
            if Xp['Host Is Superhost'].iat[index]:
                Xp['Host Is Superhost'].iat[index] = 1
            else:
                Xp['Host Is Superhost'].iat[index] = 0
        Xmod = Xp.to_numpy()
        return Xmod


class ImputeMedian(TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None):
        self.X = X
        return self

    def transform(self, X, y=None):
        for index in range(len(X)):
            change_nan_to_median(X, 'Bedrooms', 'Security Deposit', index, dict_sd)
            change_nan_to_median(X, 'Bedrooms', 'Cleaning Fee', index, dict_cf)