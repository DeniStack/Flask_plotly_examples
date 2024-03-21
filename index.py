import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import nav

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


app.validation_layout = html.Div([
    app1.layout, nav.layout, app.layout])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname in hidden_tabs:
        return html.Div()
    elif pathname == "/":
        return nav.layout
    elif pathname == '/your app location/your app name':
        return app1.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(host="your ip", port=8080, debug=False)


