import dash
from dash import html

dash.register_page(__name__, path="/aufgabe4")

layout = html.Div([
    html.H2("Aufgabe 4 - Comparison"),
    html.P("This page will allow comparing selected rows from the dataset.")
])
