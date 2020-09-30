import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State


def create_navbar():
    navbar = dbc.Navbar(
        # id="navbar",
            html.A(
                dbc.Row(
                    [
                    dbc.Col(
                        dbc.NavbarBrand(
                            'Data Pipeline Visualization',
                        )
                    )
                    ],
                ),
            href="https://plot.ly",
        ),
    color="dark",
    dark=True
    )

    return navbar