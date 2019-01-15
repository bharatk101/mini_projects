# import packages
import dash
import dash_core_components as dcc
import dash_html_components as html

# stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# init dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# colors
colors = {
    'background': '#FFDAB9',
    'text': '#EEE8AA'
}

# layout
app.layout = html.Div(children=[
    html.H1(children='Hello Dash',
            style={
                'textAlign': 'center'
            }),

    html.Div(children='''Dash : An Awesone Web Application
     Framework for Python ''',
             style={
                 'textAlign': 'center'
             }),

    # plot
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [5, 8, 1], 'type': 'bar', 'name': 'UM'}
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        })
])

# run server
if __name__ == '__main__':
    app.run_server(debug=True)
