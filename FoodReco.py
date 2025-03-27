import pandas as pd

import sys


# Receive variables from FastAPI

gender, bmi, b_sugar, b_pressure, b_cholestrol, activity_level, food_preferences = sys.argv[
    1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]


# Load data from Excel file
df = pd.read_excel('D:/nutricarenew/src/KB.xlsx')

def get_column_values(column_name):
    if column_name not in df.columns:
        return "Error: Column not found in dataframe"
    else:
        column_values = list(df[column_name])
        return column_values
