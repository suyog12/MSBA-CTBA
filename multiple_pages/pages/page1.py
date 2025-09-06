import dash
from dash import html

dash.register_page(__name__, path = "/page1", name = "Page 1")

layout = html.Div(
    [
    html.Div("Top (1 column)", className="block block--top"),
    html.Div(
        [
            html.Div("Middle Left", className="block"),
            html.Div("Middle Right", className="block"),
        ],
        className="row-2",
    ),
    html.Div("Footer", className="block block--footer"),

    html.P("This is Page 1 content.")
    ],
    className="page1-grid",
    )