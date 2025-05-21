import dash
from dash import html

dash.register_page(__name__, path="/aufgabe5")

layout = html.Div([
    html.H2("Aufgabe 5 - Analyse & Interpretation"),
    html.P("This page will include your interpretation of the results.")
])
