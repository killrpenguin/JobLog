from dash import Dash, dcc, html

app = Dash(__name__)
app.layout = html.Div([
    dcc.Input(id="jb_title", type="text", placeholder="")
]

)
