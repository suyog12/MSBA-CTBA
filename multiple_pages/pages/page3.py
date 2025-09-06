from dash import html, dcc, Input, Output, callback, register_page
import pandas as pd
import plotly.express as px
from pathlib import Path

register_page(__name__, path="/page3", name="Electricity")

DATA_PATH = Path(__file__).resolve().parent.parent / "Data" / "electricity_prices.csv"
df = pd.read_csv(DATA_PATH)

# Ensure correct types
df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# (Optional) define global min/max so the color scale doesn't jump year to year
GLOBAL_MIN = float(df["price"].min())
GLOBAL_MAX = float(df["price"].max())

layout = html.Div(
    style={"backgroundColor": "#293831", "padding": "20px"},
    children=[
        html.H1(
            "Electricity Prices by US State",
            style={"color": "#CDD6D3", "textAlign": "center"},
        ),
        dcc.Slider(
            id="year-slider",
            min=int(df["year"].min()),
            max=int(df["year"].max()),
            value=int(df["year"].min()),
            marks={str(y): str(y) for y in sorted(df["year"].dropna().unique())},
            step=None,
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        html.Br(),
        dcc.Graph(id="choropleth-map"),
    ],
)

@callback(
    Output("choropleth-map", "figure"),
    Input("year-slider", "value"),
)
def update_map(selected_year):
    # Filter year and ensure numeric
    d = df[df["year"] == selected_year].copy()
    d["price"] = pd.to_numeric(d["price"], errors="coerce")

    # Clamp to [0, 30] so the color scale is stable and meaningful
    d["price"] = d["price"].clip(lower=0, upper=30)

    # White -> light pinks -> deep red
    reds_0_30 = [
        (0.00, "#ffffff"),
        (0.05, "#fff5f5"),
        (0.20, "#fde0dd"),
        (0.40, "#fcbba1"),
        (0.60, "#fc9272"),
        (0.80, "#fb6a4a"),
        (0.95, "#de2d26"),
        (1.00, "#a50f15"),
    ]

    fig = px.choropleth(
        d,
        locations="state",
        locationmode="USA-states",
        color="price",
        scope="usa",
        color_continuous_scale=reds_0_30,  # continuous scale
        range_color=(0, 30),               # lock scale 0..30
        labels={"price": "Price (cents/kWh)"},
        title=f"Residential Electricity Prices ({selected_year})",
    )

    fig.update_traces(
        hovertemplate="State=%{location}<br>Price (cents/kWh)=%{z:.2f}<extra></extra>"
    )

    fig.update_layout(
        geo=dict(bgcolor="#B89975"),
        paper_bgcolor="#32453C",
        font_color="white",
        margin=dict(l=10, r=10, t=50, b=10),
        coloraxis_colorbar=dict(
            title="Price (cents/kWh)",
            tickvals=[0, 5, 10, 15, 20, 25, 30],
            ticks="outside",
        ),
    )
    return fig
