import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("processed_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = Dash(__name__)

fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

app.layout = html.Div([
    html.H1("Pink Morsel Visualizer"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
