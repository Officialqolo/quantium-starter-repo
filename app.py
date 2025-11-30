import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load processed CSV
df = pd.read_csv("data/formatted_sales_data.csv")
df['date'] = pd.to_datetime(df['date'])
all_regions = df['region'].unique()

# Dash app
app = dash.Dash(__name__)

# Define the application layout
app.layout = html.Div([
    html.H1("Soul Foods - Pink Morsel Sales Visualiser", style={"textAlign":"center"}),

    # Container for the dropdown filter
    html.Div([
        html.Label("Filter by Region:"),
        dcc.Dropdown(
            id='region-filter-dropdown',
            options=[{'label': region, 'value': region} for region in all_regions],
            value=all_regions,  # Default to show all regions
            multi=True,         # Allow multiple selections
            placeholder="Select a region..."
        ),
    ], style={'width': '50%', 'margin': '20px auto'}), # Center the dropdown and add spacing

    # The graph which will be updated by the callback
    dcc.Graph(id='sales-line-chart')
])

# Callback to update the graph based on the dropdown selection
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter-dropdown', 'value')
)
def update_line_chart(selected_regions):
    # If no regions are selected, use an empty dataframe to show an empty graph
    if not selected_regions:
        filtered_df = pd.DataFrame(columns=df.columns)
    else:
        filtered_df = df[df['region'].isin(selected_regions)]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        color='region',
        title='Pink Morsel Sales Over Time',
        labels={'date':'Date', 'sales':'Sales', 'region':'Region'}
    )
    fig.update_layout(transition_duration=500) # Add a smooth transition
    return fig

if __name__ == '__main__':
    app.run(debug=True)
