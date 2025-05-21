import dash
from dash import html

dash.register_page(__name__, path="/aufgabe2")

layout = html.Div([
    html.H2("Aufgabe 2 - Visualization"),
    html.P("This page will contain data visualizations.")
])
