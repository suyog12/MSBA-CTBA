import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


#initialize the app
app = dash.Dash(__name__, use_pages= True, suppress_callback_exceptions=True, title="multi page game")

server = app.server #for deployment


app.layout = html.Div([
    dbc.NavbarSimple(
        children = [
            dbc.NavLink("Home", href = "/", active = "exact"),
            dbc.NavLink("Page 1", href = "/page1", active = "exact"),
            dbc.NavLink("Page 2", href = "/page2", active = "exact"),
            dbc.NavLink("Page 3", href = "/page3", active = "exact")

        ],
    brand = "Multi-Page App"),
    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=True)