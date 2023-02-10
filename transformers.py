from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd
from functions import remove_columns, change_nan_to_median, create_median_dict
from sklearn.preprocessing import OneHotEncoder


class ImputeMedian(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None):
        self.X = X
        number_of_rooms = X['Bedrooms'].unique()
        self.dict_sd = create_median_dict(X, 'Bedrooms', 'Security Deposit', number_of_rooms)
        self.dict_cf = create_median_dict(X, 'Bedrooms', 'Cleaning Fee', number_of_rooms)
        return self

    def transform(self, X, y=None):
        for index in range(len(X)):
            change_nan_to_median(X, 'Bedrooms', 'Security Deposit', index, self.dict_sd)
            change_nan_to_median(X, 'Bedrooms', 'Cleaning Fee', index, self.dict_cf)