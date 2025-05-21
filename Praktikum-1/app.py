from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)
app.layout = html.Div([
    html.H1("Praktikum Task 1 - Interactive Dashboard"),
    dcc.Link("Home", href="/"),
    html.Br(),
    dcc.Link("Aufgabe 1", href="/aufgabe1"),
    html.Br(),
    dcc.Link("Aufgabe 2", href="/aufgabe2"),
    html.Br(),
    dcc.Link("Aufgabe 3", href="/aufgabe3"),
    html.Br(),
    dcc.Link("Aufgabe 4", href="/aufgabe4"),
    html.Br(),
    dcc.Link("Aufgabe 5", href="/aufgabe5"),
    html.Hr(),
    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=True)