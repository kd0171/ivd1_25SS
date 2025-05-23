import dash
from dash import html, dash_table
import os
import pandas as pd
from datamining.aufgabe1.cleaning import load_and_clean_data

dash.register_page(__name__, path="/aufgabe1")

# Define file paths
source_path = "./data/Praktikum-1-test-2-smallsize.csv"
output_path = "./data/processed/cleaned_data.csv"

# Load, clean, and save the data
df = load_and_clean_data(source_path, save_to=output_path)

# Convert 'Positions List' from list to string (for DataTable rendering)
if "Positions List" in df.columns:
    df["Positions List"] = df["Positions List"].apply(
        lambda x: ", ".join(x) if isinstance(x, list) else x
    )

# Page layout with table and preprocessing description
layout = html.Div([
    html.H2("Aufgabe 1 - Data Cleaning"),

    html.P(f"The dataset has been successfully cleaned and saved to '{output_path}'."),

    html.P(f"Number of rows after cleaning: {len(df)}"),
    html.P(f"Number of columns: {len(df.columns)}"),

    html.H4("Data Cleaning Steps"),
    html.Ul([
        html.Li("Column names were stripped of leading/trailing spaces and single quotes."),
        html.Li("String values in all cells were cleaned of leading/trailing spaces and single quotes."),
        html.Li("Columns starting with 'Unnamed' were removed."),
        html.Li("The 'Positions Played' column was split into a list of individual positions."),
        html.Li("No rows were dropped; incomplete data is preserved."),
    ]),

    html.H4("Preview of Cleaned Data"),
    dash_table.DataTable(
        # data=df.head(10).to_dict('records'),
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={
            'overflowX': 'auto',
            'overflowY': 'auto',
            'maxHeight': '600px',
            'border': '2px solid #333',
            'padding': '10px',
            'marginTop': '15px',
        },
        style_cell={
            'textAlign': 'left',
            'padding': '5px',
            'minWidth': '120px',
            'whiteSpace': 'normal'
        },
        style_header={
            'fontWeight': 'bold',
            'backgroundColor': '#f2f2f2',
            'borderBottom': '2px solid black'
        },
    ),
])
