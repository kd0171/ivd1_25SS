import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div([
    html.H2("Welcome to our page."),
    html.P("Gruppe 08: Kido Kenta, Schlockermann Tim")
])
