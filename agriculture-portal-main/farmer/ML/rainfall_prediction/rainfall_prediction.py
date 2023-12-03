import pandas as pd
import sys

df = pd.read_csv('C:/xampp/htdocs/agriculture-portal-main/farmer/ML/rainfall_prediction/rainfall_in_india_1901-2017.csv')

def predict_rainfall(state, month):
    state_data = df[df['SUBDIVISION'] == state]
    avg_rainfall = state_data[month].mean()
    return avg_rainfall
Jregion = "LAKSHADWEEP"
Jmonth =  "APR"

predicted_rainfall = predict_rainfall(Jregion, Jmonth)
print(predicted_rainfall)


