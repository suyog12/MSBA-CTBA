from dash import Dash, html, dcc, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-1', type='number', placeholder='Enter a number'),
    dcc.Input(id='input-2', type='number', placeholder='Enter another number'),
    dcc.Input(id='input-3', type='text', placeholder='Ener a text'),
    html.Div(id='output-1'),
    html.Div(id='output-2'),
    html.Div(id='output-3')
])

@app.callback(
    Output('output-1', 'children'),
    Output('output-2', 'children'),
    Output('output-3', 'children'),
    Input('input-1', 'value'),
    Input('input-2', 'value'),
    Input('input-3', 'value')
)

def update_outputs(num1, num2, text):
    # Handle None values
    if num1 is None:
        num1 = 0
    if num2 is None:
        num2 = 0
    if text is None:
        text = 'NA'
    #perfrom operations
    result1 = f"(The sum of {num1} and {num2} is {num1 + num2})"
    result2 = f"(The product of {num1} and {num2} is {num1 * num2})"
    result3 = f"(The reverse of '{text}' is '{text[::-1]}')"
    return result1, result2, result3

if __name__ == '__main__':
    app.run(debug=True)
