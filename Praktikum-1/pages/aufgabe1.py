import dash
from dash import html
import pandas as pd
import os

dash.register_page(__name__, path="/aufgabe1")

# Load and clean the data
df = pd.read_csv("./data/Praktikum-1-test-1-init.csv", sep=";")
df_cleaned = df.dropna()

# Save cleaned data to a shared location
os.makedirs("processed", exist_ok=True)
df_cleaned.to_csv("./data/processed/cleaned_data.csv", index=False)

layout = html.Div([
    html.H2("Aufgabe 1 - Data Cleaning"),
    html.P("Cleaned data saved to 'processed/cleaned_data.csv'.")
])
