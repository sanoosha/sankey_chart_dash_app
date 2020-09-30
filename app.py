import flask
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from plotlydash.views.layout import *
from plotlydash.views.sankeychart import  *

server = flask.Flask(__name__)

mode_bar_buttons_to_remove = [
'zoom2d',
' pan2d',
' select2d',
' lasso2d',
' zoomIn2d',
' zoomOut2d',
' autoScale2d',
' resetScale2d',
' zoom3d',
' pan3d',
' toggleHover',
' resetViews'
]

@server.route('/')
def home():
    return app.index()

app = dash.Dash(
    __name__,
    server=server,
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

df_node, df_link = create_df()

app.layout = html.Div(id='main-container',children=[
    html.Div(id='container', children=create_navbar()),
    # html.Br(),
    html.Div(
        id='sankey-chart-container',
        className="pretty-container",
        children=[
            html.P('SANKEY CHART'),
            dcc.Graph(
                id='sankey-chart',
                figure=create_sankey_chart(df_node, df_link),
                config = {'modeBarButtonsToRemove': mode_bar_buttons_to_remove}
            ),
        ]
    ),
    html.Div(
        id='datatable-chart-container',
        className="pretty-container",
        children=[
            html.P('SANKEY CHART DATATABLE'),
            create_dash_datatable(df_node, df_link)
        ]
    )
])


if __name__ == "__main__":
    server.run(host='0.0.0.0', debug=True)