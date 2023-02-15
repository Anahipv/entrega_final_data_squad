from django.shortcuts import render
from .linear_models import X_train, y_train, preprocessor
from sklearn.linear_model import RidgeCV
import pandas as pd
from math import nan

def home(request):
    return render(request, "home.html", {})

def price(request):
    df = pd.DataFrame()
    df['Host Response Rate'] = nan
    df['Neighbourhood Group Cleansed'] = [request.POST["Neighbourhood Group Cleansed"]]
    df['Property Type'] = [request.POST['Property Type']]
    df['Room Type'] = [request.POST['Room Type']]
    df['Accommodates'] = [request.POST['Guests Included']]
    df['Bathrooms'] = [request.POST['Bathrooms']]
    df['Bedrooms'] = [request.POST['Bedrooms']]
    df['Beds'] = [request.POST['Beds']]
    df['Security Deposit'] = nan
    df['Cleaning Fee'] = nan
    df['Guests Included'] = [request.POST['Guests Included']]
    df['Review Scores Rating'] = nan
    df['Cancellation Policy'] = [request.POST['Cancellation Policy']]
    df['Host Is Superhost'] = [request.POST['Host Is Superhost']]
    df['Kitchen'] = [request.POST['Kitchen']]
    df['Internet'] = [request.POST['Internet']]
    df['Air conditioning'] = [request.POST['Air conditioning']]
    df['Heating'] = [request.POST['Heating']]
    df['Washer'] = [request.POST['Washer']]
    df['Dryer'] = [request.POST['Dryer']]
    df['Elevator'] = [request.POST['Elevator']]
    df['Wheelchair accessible'] = [request.POST['Wheelchair accessible']]
    df['TV'] = [request.POST['TV'] ]
    df['Pool'] = [request.POST['Pool']]
    df['24-hour check-in'] = [request.POST['24-hour check-in']]
    X_train_prepared = preprocessor.fit_transform(X_train)
    test_prepared = preprocessor.transform(df)
    lr = RidgeCV(alphas=(0.1, 1.0, 6.6, 10.0))
    lr.fit(X_train_prepared, y_train)
    predicted_price = lr.predict(test_prepared).tolist()[0]
    lower = round(0.75*predicted_price)
    higher = round(1.25*predicted_price)
    return render(request, "price.html", {"lower": lower, "higher": higher})