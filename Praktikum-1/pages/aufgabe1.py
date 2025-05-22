import dash
from dash import html
import os
from datamining.aufgabe1.cleaning import load_and_clean_data

dash.register_page(__name__, path="/aufgabe1")

# Define file paths
source_path = "./data/Praktikum-1-test-1-init.csv"
output_path = "./data/processed/cleaned_data.csv"

# Ensure output directory exists
os.makedirs("processed", exist_ok=True)

# Load, clean, and save the data
df = load_and_clean_data(source_path, save_to=output_path)

# Page layout with confirmation message
layout = html.Div([
    html.H2("Aufgabe 1 - Data Cleaning"),
    html.P(f"The dataset has been successfully cleaned and saved to '{output_path}'."),
    html.P(f"Number of rows after cleaning: {len(df)}"),
    html.P(f"Number of columns: {len(df.columns)}")
])
