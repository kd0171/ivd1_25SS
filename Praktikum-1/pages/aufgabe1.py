import dash
from dash import html

dash.register_page(__name__, path="/aufgabe1")

layout = html.Div([
    html.H2("Aufgabe 1 - Data Cleaning"),
    html.P("This page handles CSV import and data cleaning.")
])
