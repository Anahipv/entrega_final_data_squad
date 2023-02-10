from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd
from functions import change_nan_to_median
from statistics import median
from math import isnan


class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


class ImputeMedian(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None):
        self.X = X
        dict_list_sd = {}
        dict_list_cf = {}
        for row in X:
            bedrooms = row[3]
            sd = row[5]
            cf = row[6]
            if bedrooms not in dict_list_sd:
                dict_list_sd[bedrooms] = []
                dict_list_cf[bedrooms] = []
            if not isnan(sd):
                dict_list_sd[bedrooms].append(sd)
            if not isnan(cf):    
                dict_list_cf[bedrooms].append(cf)
        self.dict_sd = {}
        self.dict_cf = {}
        for bedroom in dict_list_sd.keys():
            self.dict_sd[bedroom] = median(dict_list_sd[bedroom])
            self.dict_cf[bedroom] = median(dict_list_cf[bedroom])
        return self

    def transform(self, X, y=None):
        for row in X:
            ##sd
            if isnan(row[5]):
                bedroom = row[3]
                median = self.dict_sd[bedroom]
                row[5] = median
            ##cf
            if isnan(row[6]):
                bedroom = row[3]
                median = self.dict_cf[bedroom]
                row[6] = median
        return X