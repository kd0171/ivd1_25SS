import dash
from dash import html, dash_table
import os
import pandas as pd
from datamining.aufgabe1.cleaning import load_and_clean_data

dash.register_page(__name__, path="/aufgabe1")

# Define file paths
source_path = "./data/Praktikum-1-test-2-smallsize.csv"
output_path = "./processed/cleaned_data.csv"

# Ensure output directory exists
os.makedirs("processed", exist_ok=True)

# Load, clean, and save the data
df = load_and_clean_data(source_path, save_to=output_path)

# Page layout with table and preprocessing description
layout = html.Div([
    html.H2("Aufgabe 1 - Data Cleaning"),

    html.P(f"The dataset has been successfully cleaned and saved to '{output_path}'."),

    html.P(f"Number of rows after cleaning: {len(df)}"),
    html.P(f"Number of columns: {len(df.columns)}"),
        
    html.H4("Data Cleaning Steps"),
    html.Ul([
        html.Li("Column names were stripped of spaces and single quotes."),
        html.Li("String values in each cell were cleaned of leading/trailing spaces and single quotes."),
        html.Li("Columns starting with 'Unnamed' were removed."),
        html.Li("If the 'Nationality' column contains a position (e.g. 'ST', 'GK', etc.), "
                "values from that column onward are shifted left until 'Nationality' is no longer a position."),
        html.Li("No rows were dropped; partial data is preserved."),
    ]),

    html.H4("Preview of Cleaned Data"),
    dash_table.DataTable(
        data=df.head(100).to_dict('records'),  # show first 10 rows
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '5px'},
        style_header={'fontWeight': 'bold'}
    ),
])
