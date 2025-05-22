import plotly.express as px

def plot_position_distribution(df):
    return px.histogram(df, x="Positions Played", title="Distribution of Positions")

def plot_age_vs_wage(df):
    return px.scatter(df, x="Age", y="Wage(in Euro)", title="Age vs Wage", hover_name="Full Name")

def plot_age_vs_overall(df):
    return px.scatter(df, x="Age", y="Overall", title="Age vs Overall", hover_name="Full Name")
