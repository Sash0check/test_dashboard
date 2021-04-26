import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
data = pd.read_csv("data.csv")

app = dash.Dash()
server = app.server
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': data['x'].values, 'y': data['y'].values, 'type': 'bar', 'name': 'SF'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
