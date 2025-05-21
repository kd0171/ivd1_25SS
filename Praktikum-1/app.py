import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Initialize Dash app with Bootstrap theme and page support
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define navigation bar using Bootstrap components
navbar = dbc.NavbarSimple(
    brand="Praktikum 1",
    brand_href="/",
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Aufgabe 1", href="/aufgabe1")),
        dbc.NavItem(dbc.NavLink("Aufgabe 2", href="/aufgabe2")),
        dbc.NavItem(dbc.NavLink("Aufgabe 3", href="/aufgabe3")),
        dbc.NavItem(dbc.NavLink("Aufgabe 4", href="/aufgabe4")),
        dbc.NavItem(dbc.NavLink("Aufgabe 5", href="/aufgabe5")),  # Use /analyse if page is registered as that
    ]
)

# Define overall layout including navbar and dynamic page content
app.layout = html.Div([
    navbar,
    dbc.Container(dash.page_container, className="pt-4")  # Render current page here
])

# Start the Dash server
if __name__ == "__main__":
    app.run(debug=True)
