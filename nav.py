import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output




content = html.Div(
    [
        html.Div(className="container", children=[
            html.H1("Your Report App", className="my-4 text-center display-4"),
            dbc.Row(style={"margin-bottom": "25px"},
                    children=[
                        html.Div(className="col-lg-3", children=[
                            html.Div(className="card h-100 shadow", children=[
                                html.Div(className="card-body", children=[
                                    html.H5(className="card-title", children=[
                                        html.A(href="/your location to the file/name of the file", children=[
                                            html.Div("Your app", style={"text-align": "center"}),
                                        ], )
                                    ]),
                                ]),
                            ]),
                        ]),
                        # Placeholder for another card
                        html.Div(className="col-lg-3", children=[
                            html.Div(className="card h-100 shadow", children=[
                                html.Div(className="card-body", children=[
                                    html.H5(className="card-title", children=[
                                        html.Div("Example Placeholder", style={"text-align": "center"}),
                                    ]),
                                ]),
                            ]),
                        ]),
                    ])
                ]),
            ]),
        ]),
    ],
    id="content"
)


layout = html.Div([content])

#After you start teh file this will be the menu for the apps

