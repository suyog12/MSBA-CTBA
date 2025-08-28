# we are ceating a website
# it does not render into github without a render repo
# built on top of Plotly, Flask and React
# Dash is for Data analysts/scientists
# hgh customization in dasah than in others
# it outputs to webpage
# it uses HTML, CSS and JS
# dash can handle static and dynamic content
    # user interaction, query of a databse, API call, reallife straming
# dash handls callback with app @app.callback()
# we deal with amjority of API call
# we need to import

# just saying padding wil;l change top, left right, button

from dash import Dash, html

app = Dash(__name__)
app.title = "My First Dash App" 
# app.layout = html.Div("Hello Dash") # definig the layout of the app
app.layout = html.Div([
    html.H1("Hello Dash",
            style={"color": "#381D8C", # customizing the header
                   "fontsize": "20px", # font size
                 #  "textAlign": "center", # text alignment
                   "backgroundColor": "#AA6171" # background color
                   }
            ), # adding a header
    html.P("This is a simple dashboard",
           style={"color": "#2CC690",
                  "padding": "30px",
                  "margin": "10px",
                    "border": "2px solid #C65D2C"
                  }
           ), # adding a paragraph
    html.Br(), # adding a line break
    html.A("Click here to go to Google", 
           href="https://www.google.com",
            target="_blank",  # Opens in a new tab
        ) # adding a link    
])  


if __name__ == "__main__":
    app.run(debug=True, use_reloader = True) # running the app in debug mode
    
    ##html.Div() is a container for other HTML elements
    ##html.H1() is a header element
    ##html.P() is a paragraph element  
    ##app.run() runs the app
    ##html.render() renders the app in the browser