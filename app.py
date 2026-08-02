import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# 1. Load formatted data
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date")

# 2. Initialize Dash app
app = Dash(__name__)

# Custom color palette (Soul Foods theme)
COLORS = {
    "background": "#1E1E2E",
    "card_bg": "#2A2A3D",
    "text": "#F5F5F7",
    "accent": "#FF6B8B",
    "grid": "#3A3A52"
}

# Helper function to generate figure
def generate_chart(filtered_df):
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Pink Morsels Sales Performance Over Time",
        labels={"date": "Date", "sales": "Total Sales ($)"}
    )
    fig.update_traces(line_color=COLORS["accent"], line_width=2.5)
    fig.update_layout(
        plot_bgcolor=COLORS["card_bg"],
        paper_bgcolor=COLORS["card_bg"],
        font_color=COLORS["text"],
        title_font_size=22,
        title_x=0.5,
        xaxis=dict(showgrid=True, gridcolor=COLORS["grid"]),
        yaxis=dict(showgrid=True, gridcolor=COLORS["grid"]),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig

# 3. App Layout
app.layout = html.Div(
    style={
        "backgroundColor": COLORS["background"],
        "minHeight": "100vh",
        "padding": "40px 20px",
        "fontFamily": "'Segoe UI', Roboto, Helvetica, Arial, sans-serif",
        "color": COLORS["text"]
    },
    children=[
        # Header Section
        html.Div(
            style={"textAlign": "center", "marginBottom": "30px"},
            children=[
                html.H1(
                    "Soul Foods — Pink Morsels Visualiser",
                    style={"color": COLORS["accent"], "fontWeight": "700", "marginBottom": "8px"}
                ),
                html.P(
                    "Track sales trends across regions before and after the price increase on Jan 15, 2021.",
                    style={"fontSize": "16px", "color": "#A0A0B2"}
                )
            ]
        ),

        # Region Filter (Radio Buttons)
        html.Div(
            style={
                "backgroundColor": COLORS["card_bg"],
                "padding": "20px",
                "borderRadius": "12px",
                "maxWidth": "800px",
                "margin": "0 auto 30px auto",
                "boxShadow": "0 8px 16px rgba(0,0,0,0.3)",
                "textAlign": "center"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "600", "fontSize": "18px", "marginBottom": "12px", "display": "block"}
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"}
                    ],
                    value="all",
                    inline=True,
                    inputStyle={"marginRight": "6px", "marginLeft": "16px"},
                    style={"fontSize": "16px"}
                )
            ]
        ),

        # Chart Container
        html.Div(
            style={
                "backgroundColor": COLORS["card_bg"],
                "padding": "20px",
                "borderRadius": "12px",
                "maxWidth": "1000px",
                "margin": "0 auto",
                "boxShadow": "0 8px 16px rgba(0,0,0,0.3)"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# 4. Dynamic callback to update graph based on region choice
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.groupby("date", as_index=False)["sales"].sum()
    else:
        filtered_df = df[df["region"] == selected_region]

    return generate_chart(filtered_df)

# Updated runner method (fixes ObsoleteAttributeException)
if __name__ == "__main__":
    app.run(debug=True)