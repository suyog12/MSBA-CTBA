import datetime as dt
import requests
from dash import Dash, html, dcc, Input, Output, exceptions

API_KEY = "DEMO_KEY"          # Replace with your own if you have one
APOD_URL = "https://api.nasa.gov/planetary/apod" # NASA Astronomy Picture of the Day API endpoint
MIN_DATE = dt.date(1995, 6, 16) # APOD started on June 16, 1995
TODAY = dt.date.today() # Today's date

app = Dash(__name__) # creating a Dash application
app.title = "NASA APOD" # setting the title of the app

app.layout = html.Div( # main container
    style={"margin": "0 auto", # center the container
           "padding":20  # padding around the container
           },# styling the container
    children=[ # children elements
        html.H1("NASA Astronomy Picture of the Day"), # header
        html.P("Select a date to see the APOD for that day."), # paragraph
        dcc.DatePickerSingle( # date picker component
            id="apod-date", # id of the date picker
            min_date_allowed=MIN_DATE, # minimum date allowed
            max_date_allowed=TODAY, # maximum date allowed
            date=TODAY, # default date
            display_format="YYYY-MM-DD", # date format
            clearable=False, # cannot clear the date
            style={"border": "0px solid black"} # styling the date picker
        ),
        dcc.Loading(html.Div(id="media", # div to display media
                             style={"marginTop": 16, # margin top
                                    "textAlign": "center" # center the content
                                    } # styling the div
                             ) # loading component to show loading state
                    ), # loading component to show loading state
        html.Div(id="caption"), # div to display caption
    ], # children of the main container
) # main container

@app.callback(
    [Output("media", "children"), 
     Output("caption", "children")
    ],
    Input("apod-date", "date"),
)
def show_apod(date_str):
    if not date_str:
        raise exceptions.PreventUpdate

    try:
        date_obj = dt.date.fromisoformat(date_str[:10])
    except Exception:
        return "Invalid date.", ""

    params = {"api_key": API_KEY, "date": date_obj.isoformat()}
    try:
        r = requests.get(APOD_URL, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as e:
        return f"API error: {e}", ""

    media_type = data.get("media_type", "")
    url = data.get("url", "")
    title = data.get("title", "APOD")
    explanation = data.get("explanation", "")

    if media_type == "image":
        media = html.Img(src=url, style={"maxWidth": "100%", "borderRadius": 8}, alt=title)
    elif media_type == "video":
        media = html.Iframe(src=url, style={"width": "100%", "height": 500, "border": 0})
    else:
        media = html.Div("Unsupported media type.")

    header = html.H3(f"{title} — {date_obj.isoformat()}", style={"marginBottom": 8})
    return html.Div([header, media]), explanation

if __name__ == "__main__":
    app.run(debug=True)