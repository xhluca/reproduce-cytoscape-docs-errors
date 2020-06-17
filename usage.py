import dash
import dash_cytoscape as cyto
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20*lat, 'y': -20*long}
    }
    for short, label, long, lat in (
        ('la', 'Los Angeles', 34.03, -118.25),
        ('nyc', 'New York', 40.71, -74),
        ('to', 'Toronto', 43.65, -79.38),
        ('mtl', 'Montreal', 45.50, -73.57),
        ('van', 'Vancouver', 49.28, -123.12),
        ('chi', 'Chicago', 41.88, -87.63),
        ('bos', 'Boston', 42.36, -71.06),
        ('hou', 'Houston', 29.76, -95.37)
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('van', 'la'),
        ('la', 'chi'),
        ('hou', 'chi'),
        ('to', 'mtl'),
        ('mtl', 'bos'),
        ('nyc', 'bos'),
        ('to', 'hou'),
        ('to', 'nyc'),
        ('la', 'nyc'),
        ('nyc', 'bos')
    )
]

elements = nodes + edges


app.layout = html.Div([
    html.Button('show network', id='button', n_clicks=0),

    html.Div(id='cytoscape-div', style={'display': 'none'}, children=[
        cyto.Cytoscape(
            id='cytoscape-layout-2',
            elements=elements,
            style={'width': '100%', 'height': '350px'},
            layout={
                'name': 'circle'
            }
        )
    ]),
])

@app.callback(Output('cytoscape-div', 'style'), [Input('button', 'n_clicks')])
def show_network(n_clicks):
    if n_clicks % 2 == 1:
        print(n_clicks)
        return {'display': 'none'}
    return {'display': 'block'}

if __name__ == '__main__':
    app.run_server(debug=True)
