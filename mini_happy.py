from dash import Dash, html

app= Dash(__name__)

app.layout = html.Div([
    html.H1("World Happiness Dashboard",
            style={"color": "#381D8C", # customizing the header
                   "textAlign": "center", # text alignment
            }
            ), # adding a header
    html.P("This is a World Happiness Report Dashboard",
              style={"color": "#2CC690",
                    "padding": "30px",
                    "margin": "10px",
                      "border": "2px solid #C65D2C"
                    }
              ), # adding a paragraph
    html.Br(), # adding a line break
    html.A("Click here to go to World Happiness Report", 
           href="https://www.worldhappiness.report/",
            target="_blank",  # Opens in a new tab
        ) # adding a link 
])
                      
if __name__ == "__main__":
    app.run(debug=True, use_reloader = True) # running the app in debug mode   