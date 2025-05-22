import dash
from dash import html, dcc, Input, Output
import pandas as pd
from datamining.aufgabe2.graphing import (
    plot_position_distribution,
    plot_age_vs_wage,
    plot_age_vs_overall
)

dash.register_page(__name__, path="/aufgabe2")

df = pd.read_csv("./processed/cleaned_data.csv")

layout = html.Div([
    html.H2("Aufgabe 2 - Data Visualization"),

    html.Label("Select a chart to display:"),
    dcc.Dropdown(
        id="chart-dropdown",
        options=[
            {"label": "Position Distribution", "value": "position"},
            {"label": "Age vs Wage", "value": "age_wage"},
            {"label": "Age vs Overall", "value": "age_overall"},
        ],
        value="position"  # Default selection
    ),

    dcc.Graph(id="chart-output")
])

# --- Callback to switch figures ---
@dash.callback(
    Output("chart-output", "figure"),
    Input("chart-dropdown", "value")
)
def update_chart(selected_chart):
    if selected_chart == "age_wage":
        return plot_age_vs_wage(df)
    elif selected_chart == "age_overall":
        return plot_age_vs_overall(df)
    else:
        return plot_position_distribution(df)
