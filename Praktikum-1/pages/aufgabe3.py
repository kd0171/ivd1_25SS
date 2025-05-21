import dash
from dash import html

dash.register_page(__name__, path="/aufgabe3")

layout = html.Div([
    html.H2("Aufgabe 3 - Interaction"),
    html.P("This page will include interactive filters.")
])
