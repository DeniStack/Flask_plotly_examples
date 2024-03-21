import dash
import dash_bootstrap_components as dbc
import dash_auth
import user_mgmt

#app = dash.Dash(external_stylesheets=[dbc.themes.COSMO])
app = dash.Dash(__name__)
server = app.server
app.title = "Your example report"
auth = dash_auth.BasicAuth(
    app,
    user_mgmt.read_users()
)