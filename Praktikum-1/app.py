from dash import Dash, html
from aufgabe1.cleaning import clean_data

# Initialize Dash app
app = Dash(__name__)

# Load cleaned dataset
df = clean_data("aufgabe1/data/Praktikum-1-test-1-init.csv")

# Define app layout
app.layout = html.Div([
    html.H1("Data Preview"),
    html.P(f"Number of rows: {len(df)}"),
    html.P(f"Number of columns: {len(df.columns)}"),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
