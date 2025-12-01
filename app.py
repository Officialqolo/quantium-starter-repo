import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load processed CSV
df = pd.read_csv("data/formatted_sales_data.csv")
df['date'] = pd.to_datetime(df['date'])

# Create line chart
fig = px.line(
    df,
    x='date',
    y='sales',
    color='region',
    title='Pink Morsel Sales Over Time',
    labels={'date':'Date', 'sales':'Sales', 'region':'Region'}
)

# Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Soul Foods - Pink Morsel Sales Visualiser", style={"textAlign":"center"}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
