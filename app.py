import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# -------------------------
# Load processed data
# -------------------------
DATA_PATH = "./processed_data.csv"
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# -------------------------
# Initialize Dash app
# -------------------------
app = Dash(__name__)

# -------------------------
# Layout with Modern Design
# -------------------------
app.layout = html.Div(
    style={
        "fontFamily": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "minHeight": "100vh",
        "padding": "0",
        "margin": "0",
    },
    children=[
        # Header Section
        html.Div(
            style={
                "background": "rgba(255, 255, 255, 0.98)",
                "backdropFilter": "blur(10px)",
                "padding": "32px 48px",
                "boxShadow": "0 4px 24px rgba(0, 0, 0, 0.08)",
                "borderBottom": "1px solid rgba(102, 126, 234, 0.1)",
            },
            children=[
                html.Div(
                    style={
                        "maxWidth": "1400px",
                        "margin": "0 auto",
                        "display": "flex",
                        "alignItems": "center",
                        "justifyContent": "space-between",
                    },
                    children=[
                        html.Div([
                            html.H1(
                                "Pink Morsel",
                                style={
                                    "margin": "0",
                                    "fontSize": "36px",
                                    "fontWeight": "700",
                                    "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                                    "WebkitBackgroundClip": "text",
                                    "WebkitTextFillColor": "transparent",
                                    "letterSpacing": "-0.5px",
                                },
                            ),
                            html.P(
                                "Sales Analytics Dashboard",
                                style={
                                    "margin": "4px 0 0 0",
                                    "fontSize": "15px",
                                    "color": "#64748b",
                                    "fontWeight": "500",
                                },
                            ),
                        ]),
                        html.Div(
                            style={
                                "display": "flex",
                                "alignItems": "center",
                                "gap": "12px",
                            },
                            children=[
                                html.Div(
                                    style={
                                        "width": "10px",
                                        "height": "10px",
                                        "borderRadius": "50%",
                                        "background": "#10b981",
                                        "boxShadow": "0 0 0 4px rgba(16, 185, 129, 0.2)",
                                    }
                                ),
                                html.Span(
                                    "Live Data",
                                    style={
                                        "fontSize": "14px",
                                        "color": "#64748b",
                                        "fontWeight": "500",
                                    },
                                ),
                            ],
                        ),
                    ],
                )
            ],
        ),
        # Main Content Container
        html.Div(
            style={
                "maxWidth": "1400px",
                "margin": "0 auto",
                "padding": "40px 48px",
            },
            children=[
                # Control Panel Card
                html.Div(
                    style={
                        "background": "rgba(255, 255, 255, 0.98)",
                        "backdropFilter": "blur(10px)",
                        "borderRadius": "16px",
                        "padding": "28px 32px",
                        "marginBottom": "32px",
                        "boxShadow": "0 8px 32px rgba(0, 0, 0, 0.08)",
                        "border": "1px solid rgba(255, 255, 255, 0.8)",
                        "transition": "all 0.3s ease",
                    },
                    children=[
                        html.Div(
                            style={
                                "display": "flex",
                                "alignItems": "center",
                                "justifyContent": "space-between",
                                "flexWrap": "wrap",
                                "gap": "20px",
                            },
                            children=[
                                html.Div([
                                    html.Label(
                                        "Region Filter",
                                        style={
                                            "fontSize": "14px",
                                            "fontWeight": "600",
                                            "color": "#475569",
                                            "textTransform": "uppercase",
                                            "letterSpacing": "0.5px",
                                            "marginBottom": "12px",
                                            "display": "block",
                                        },
                                    ),
                                    dcc.RadioItems(
                                        id="region-filter",
                                        options=[
                                            {"label": "All Regions", "value": "all"},
                                            {"label": "North", "value": "north"},
                                            {"label": "East", "value": "east"},
                                            {"label": "South", "value": "south"},
                                            {"label": "West", "value": "west"},
                                        ],
                                        value="all",
                                        inline=True,
                                        style={
                                            "display": "flex",
                                            "gap": "24px",
                                            "flexWrap": "wrap",
                                        },
                                        labelStyle={
                                            "display": "flex",
                                            "alignItems": "center",
                                            "cursor": "pointer",
                                            "fontSize": "15px",
                                            "fontWeight": "500",
                                            "color": "#334155",
                                            "padding": "8px 20px",
                                            "borderRadius": "8px",
                                            "transition": "all 0.2s ease",
                                            "border": "2px solid #e2e8f0",
                                        },
                                        inputStyle={
                                            "marginRight": "8px",
                                            "accentColor": "#667eea",
                                            "width": "18px",
                                            "height": "18px",
                                            "cursor": "pointer",
                                        },
                                    ),
                                ]),
                            ],
                        )
                    ],
                ),
                # Chart Card
                html.Div(
                    style={
                        "background": "rgba(255, 255, 255, 0.98)",
                        "backdropFilter": "blur(10px)",
                        "borderRadius": "16px",
                        "padding": "32px",
                        "boxShadow": "0 8px 32px rgba(0, 0, 0, 0.08)",
                        "border": "1px solid rgba(255, 255, 255, 0.8)",
                    },
                    children=[dcc.Graph(id="sales-chart", config={"displayModeBar": False})],
                ),
            ],
        ),
    ],
)

# -------------------------
# Callback for filtering
# -------------------------
@app.callback(Output("sales-chart", "figure"), Input("region-filter", "value"))
def update_chart(region):
    if region == "all":
        df = data
    else:
        df = data[data["region"] == region]

    fig = px.line(
        df,
        x="date",
        y="sales",
        title=f"Sales Performance – {region.capitalize() if region != 'all' else 'All Regions'}",
        markers=True,
        color_discrete_sequence=["#667eea"],
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8, line=dict(width=2, color="white")),
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>",
    )

    fig.update_layout(
        plot_bgcolor="rgba(248, 250, 252, 0.5)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        title_font={
            "size": 24,
            "color": "#1e293b",
            "family": "Inter, sans-serif",
            "weight": 700,
        },
        title_x=0,
        title_pad={"b": 20},
        xaxis_title="Date",
        yaxis_title="Sales Revenue",
        xaxis=dict(
            showgrid=True,
            gridcolor="rgba(148, 163, 184, 0.1)",
            gridwidth=1,
            title_font=dict(size=14, color="#64748b", weight=600),
            tickfont=dict(size=12, color="#64748b"),
            showline=True,
            linecolor="rgba(148, 163, 184, 0.2)",
            linewidth=1,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(148, 163, 184, 0.15)",
            gridwidth=1,
            title_font=dict(size=14, color="#64748b", weight=600),
            tickfont=dict(size=12, color="#64748b"),
            tickformat="$,.0f",
            showline=True,
            linecolor="rgba(148, 163, 184, 0.2)",
            linewidth=1,
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="rgba(255, 255, 255, 0.95)",
            bordercolor="#667eea",
            font_size=13,
            font_color="#334155",
        ),
        margin=dict(l=60, r=40, t=80, b=60),
        font=dict(family="Inter, sans-serif"),
    )

    return fig


# -------------------------
# Run app
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)