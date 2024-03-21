# Import necessary libraries and modules
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import datetime
import pandas as pd
# These imports are custom modules or configurations from your application
from app import app  # Flask application
import mssql_queries  # SQL queries for Microsoft SQL Server
import mssql_conn  # Connection to Microsoft SQL Server
import constants  # Constants used in the application
import mysql_queries  # SQL queries for MySQL
import io
import base64

# Controls section containing input components like date pickers, database dropdown, and submit button
controls = dbc.FormGroup(
    [
        # Date and time pickers for start and end time
        dbc.Row([
            dbc.Col(
            html.Div(["Start Time: ", constants.start_date_picker]),  # Start date picker
                ),
            dbc.Col(
                    constants.start_time_picker  # Start time picker
            )
        ],style={"marginBottom":"0.5em"}),
        dbc.Row([
            dbc.Col(
            html.Div(["End Time: ", constants.end_date_picker]),  # End date picker
                ),
            dbc.Col(
                    constants.end_time_picker  # End time picker
                ),
        ]),
        html.Hr(),  # Horizontal line
        dbc.Row([
            dbc.Col([
                    html.Div(["Database"])  # Database label
            ]),
            dbc.Col([
                    constants.database  # Dropdown for selecting database
            ])
        ],style={"marginBottom":"2em"}),
        dbc.Button(
            id='submit_button3',  # Button ID
            n_clicks=0,  # Initial number of clicks
            children='Submit',  # Button label
            color='primary',  # Button color
            block=True  # Button takes full width
            ),
        html.Hr(),  # Horizontal line
        html.Div(id="alert4"),  # to show report for user
        html.Div(id="bar_chart"), #to show bar chart
        html.Div(id="link4"),  # Links to excel download also to excel_data
    ]
)

# Sidebar containing controls
sidebar = html.Div(
    [
        html.H2('Parameters', style=constants.TEXT_STYLE),  # Sidebar title
        html.Hr(),  # Horizontal line
        controls  # Controls section
    ],
    style=constants.SIDEBAR_STYLE,  # Sidebar style
)

# Main content section
content = html.Div(
    [
        html.H1("User Log Report", style={"text-align": "center"}),  # Page title
        dcc.Tabs(
            [
                dcc.Tab(
                    label="Report",
                    children=[
                        dcc.Store(id="user_data"),  # appcallback output 2
                        html.Div(id="users"),  # Placeholder for user log table
                        dcc.Store("excel_data"), #links to callback for excel
                        dcc.Store("Bar_chart_link"),#links to bar chart callback
                        html.Div(id="table1"),
                        html.Hr(),
                        dbc.Row([], style={"marginBottom": "0.5em"}),
                    ],
                ),
                dcc.Tab(
                    label="Daily",
                    children=[
                        dcc.Graph(
                            id="Bar_chart", style={"height": 800}#Linked to the bar chart callback
                        ),  
                        dcc.Store(id="excel_data"),
                    ],
                ),  # <-- Added closing parentheses here
                # ),#Here you can add like this more tabs
                # dcc.Tab(
                    # label="Placeholder",
                    # children=[
                        # dcc.Graph(
                            # id="bar_chart2", style={"height": 800}
                        # ),  # appcallback pie output 1
                        # dcc.Store(id="placeholder"),
                    # ],
                # ),
            ]
        ),
    ],
    style=constants.CONTENT_STYLE,
    id="content",
)


# Layout combining sidebar and main content
layout = html.Div([sidebar, content])

# Callback to update user log table, Excel data, and alert message based on button click and input values
@app.callback(
    [
        Output("users", "children"), 
        Output("users_data", "data"), 
        Output("alert4", "children"), 
        Output("excel_data", "data"), 
    ],
    [Input("submit_button3", "n_clicks")],
    state=[
        State("start_date_picker", "date"), State("start_time_picker", "value"),
        State("end_date_picker", "date"), State("end_time_picker", "value"),
        State("database", "value")
    ]
)
def show_users(n_clicks, start_date_picker, start_time_picker, end_date_picker, end_time_picker, database):
    if n_clicks:
        # Convert start and end time to datetime objects
        start_time = datetime.datetime.strptime(start_date_picker, "%Y-%m-%d") + datetime.timedelta(hours=int(start_time_picker[0:2]))
        end_time = datetime.datetime.strptime(end_date_picker, "%Y-%m-%d") + datetime.timedelta(hours=int(end_time_picker[0:2]))
        parameters = [start_time, end_time]

        # Build SQL query string and execute query to fetch user log data
        query_string = mssql_queries.build_db_query_string_app1()
        records = mssql_conn.execute_query(query_string, parameters, str(database))

        if records:
            # Convert fetched records to DataFrame and format columns
            dataframe = pd.DataFrame.from_records(records)
            dataframe.columns = ["Your database example","Timestamp example", "Worker name", "Worker pin"]
            return dbc.Table.from_dataframe(dataframe), dataframe.to_json(date_format='iso', orient='split'), None
        else:
            return None, None, dbc.Alert("No entries within the specified timeframe.", color="warning", duration=5000)
    else:
        return dbc.Table(None), None, None


#creates a bar chart
@app.callback(
    Output("Bar_chart", "figure"),
    [Input("intermediate-value1", "data")],
    [
        State("start_date_picker", "date"),
        State("start_time_picker", "value"),
        State("end_date_picker", "date"),
        State("end_time_picker", "value"),
        State("database", "value"),
        State("language", "value"),
    ],
)
def create_bar_chart(
    n_clicks,
    start_date_picker,
    start_time_picker,
    end_date_picker,
    end_time_picker,
    database,
    language,
):
    if n_clicks:
        start_time = datetime.datetime.strptime(
            start_date_picker, "%Y-%m-%d"
        ) + datetime.timedelta(hours=int(start_time_picker[0:2]))
        end_time = datetime.datetime.strptime(
            end_date_picker, "%Y-%m-%d"
        ) + datetime.timedelta(hours=int(end_time_picker[0:2]))
        parameters = [start_time, end_time]
        query_string = mssql_queries.build_db_query_app7(str(language))
        records = mssql_conn.execute_query(query_string, parameters, str(database))
        if records:
            dataframe = pd.DataFrame.from_records(records)
            dataframe.columns = ["Your database example","Timestamp example", "Worker name", "Worker pin"]
            

            # Group by Timestamp and sum Duration
            dataframe["Worker Timestamp"] = pd.to_datetime(dataframe["Worker Timestamp"]).dt.date
            dataframe = dataframe.groupby("Worker Timestamp")["Duration"].sum().reset_index()

            fig = px.bar(
                dataframe,
                x=dataframe["Worker Timestamp"],
                y=dataframe["Duration"],
                title=("Shift in minutes:") + " " + (database),
            )
            fig.update_xaxes(
                dtick="D1",
                tickformat="%d-%m-%Y",
            )

            return go.Figure(fig)
        else:
            fig = {}
    else:
        fig = {}
        # return dbc.Table.from_dataframe(dataframe), dataframe.to_json(date_format="iso", orient="split"), None




# Callback to generate and display download link for Excel sheet
@app.callback(Output('link', 'children'), [Input("excel_data", "data")],
              state=[State("start_date_picker", "date"), State("start_time_picker", "value"),
                     State("end_date_picker", "date"), State("end_time_picker", "value"),
                     State("database", "value")])
def download_sheet(output, start_date_picker, start_time_picker, end_date_picker, end_time_picker, database):
    if not output:
        return None
    # Read JSON data and convert to DataFrame
    df = pd.read_json(output, orient='split')
    # Convert 'Timestamp' column to datetime and remove timezone
    df["Timestamp"] = df["Timestamp"].dt.tz_localize(None)

    # Parse the date and time parameters to create start and end timestamps
    start_time = datetime.datetime.strptime(start_date_picker, "%Y-%m-%d") + datetime.timedelta(hours=int(start_time_picker[0:2]))
    end_time = datetime.datetime.strptime(end_date_picker, "%Y-%m-%d") + datetime.timedelta(hours=int(end_time_picker[0:2]))

    # Read JSON data and convert it to a DataFrame
    df = pd.read_json(output, orient='split')

    # Convert 'Timestamp' column to datetime and remove timezone
    df["Timestamp"] = df["Timestamp"].dt.tz_localize(None)

    # Create an in-memory IO buffer for Excel file storage
    xlsx_io = io.BytesIO()

    # Create an Excel writer object
    writer = pd.ExcelWriter(xlsx_io, engine='xlsxwriter', options={"remove_timezone" : True})

    # Write DataFrame to Excel sheet
    df.to_excel(writer, sheet_name="User Log")

    # Save the Excel file
    writer.save()

    # Reset the pointer of the IO buffer to the beginning
    xlsx_io.seek(0)

    # Define media type and encode the Excel file to base64
    media_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    data = base64.b64encode(xlsx_io.read()).decode("utf-8")

    # Define download link properties
    href_data_downloadable = f'data:{media_type};base64,{data}'
    file_name = "User_Log-{0}-{1}_{2}.xlsx".format(str(database), start_time, end_time)

    # Return the download link
    return html.A("Download Excel Sheet", download=file_name, href=href_data_downloadable)
    
    
    #App_users explained

    # Parameters Sidebar: Users can specify the start and end time for the log data they want to analyze. 
    #They can select the database from which they want to fetch the data using a dropdown menu. After setting the parameters, users can click the "Submit" button to trigger the analysis.

    # User Log Display: The main content area displays a table containing the user log data based on the selected parameters. If no data is found within the specified timeframe, a warning message is displayed instead.

    # Download Excel Sheet: Users have the option to download the displayed user log data as an Excel sheet. Upon clicking the "Download Excel Sheet" link, an Excel file containing the user log data is generated and made available for download.

    # Functionality:
        # The application fetches user log data from a Microsoft SQL Server database based on the specified parameters.
        # It formats the fetched data into a tabular format and displays it to the user.
        # Additionally, it provides the functionality to download the displayed user log data as an Excel file for further analysis or reporting.

# #This application provides a convenient way for users to analyze and download user log data from a SQL Server database, enabling them to gain insights and perform further analysis as needed.