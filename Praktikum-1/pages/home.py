import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div([
    html.H2("Welcome to Praktikum Task 1"),
    html.P("Select a task from the menu to begin.")
])
