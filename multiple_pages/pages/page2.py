import dash
from dash import html, dcc, callback, Output, Input
import requests

dash.register_page(__name__, path="/page2", name="Page 2")

layout = html.Div([
    html.H2("Page 2", className="page-title"),
    html.P("Click to fetch a random cat fact from a public API.", className="page-subtitle"),
    html.Button("Get Cat Fact", id="btn-cat", n_clicks=0),
    dcc.Loading(html.Div(id="cat-fact"))
])

# Callback to fetch cat fact
@callback(
    Output("cat-fact", "children"),
    Input("btn-cat", "n_clicks")
)
def fetch_cat_fact(n_clicks):
    if n_clicks == 0:
        return "Press the button to see a cat fact."
    try:
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()
        return data.get("fact", "No fact found!")
    except Exception as e:
        return f"Error fetching cat fact: {e}"
