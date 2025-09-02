# callback_example.py
from dash import Dash, html, dcc, Input, Output, callback

app = Dash(__name__) # creating a Dash application
app.title = "Callback Example"

app.layout = html.Div(
    style={"maxWidth": 900, # max width of the container
           "margin": "40px auto", # centering the container
           "fontFamily": "Georgia, serif" # font family
           }, # styling the container
    children=[
        html.H1("Callback Example"), # header
        html.Ul([
            html.Li(["Input box’s ", # list item
                     html.Code("value"), # code element
                     " property updates output text" # text element"
                     ])
        ]), # unordered list
        dcc.Input(
            id="text-in", # input box with id
            type="text",# type of input
            placeholder="type here…",# placeholder text
            style={"width": "100%", # full width 
                   "fontSize": "48px", # font size
                   "padding": "8px" # padding
                   },# styling the input box
        ), # input box
        html.Div(id="text-out", # output div with id
                 style={"fontSize": "64px", # font size
                        "marginTop": "20px" # margin top
                        } # styling the output div
                 ),# output div
    ],
)

@callback(Output(component_id="text-out",  # output div id
                 component_property="children" # output div property
                 ),
          Input(component_id="text-in", # input box id
                component_property="value" # input box property
                ))
def show_text(value): # callback function
    return f"Text: {value or ''}" # return the input value or empty string

if __name__ == "__main__": 
    app.run(debug=True)    # running the app in debug mode