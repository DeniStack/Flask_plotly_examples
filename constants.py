import dash_core_components as dcc
import datetime

SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '25%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'top': 0,
    'padding': '20px 10px'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}
#Here are constants that are your style

start_date_picker = dcc.DatePickerSingle(
                        id='start_date_picker',
                        min_date_allowed=datetime.date(2021, 1, 1),
                        max_date_allowed=datetime.date(2024, 12, 31),
                        #initial_visible_month=datetime.date(2010, 10, 12),
                        date=datetime.date.today() - datetime.timedelta(days=1),
                        display_format = "DD-MM-YYYY")
#Here are constants that are going to be your date pickers in the ui

start_time_picker = dcc.Dropdown(
                        id='start_time_picker',
                        options=[
                            {'label': '00:00', 'value': '00:00'},
                            {'label': '01:00', 'value': '01:00'},
                            {'label': '02:00', 'value': '02:00'},
                            {'label': '03:00', 'value': '03:00'},
                            {'label': '04:00', 'value': '04:00'},
                            {'label': '05:00', 'value': '05:00'},
                            {'label': '06:00', 'value': '06:00'},
                            {'label': '07:00', 'value': '07:00'},
                            {'label': '08:00', 'value': '08:00'},
                            {'label': '09:00', 'value': '09:00'},
                            {'label': '10:00', 'value': '10:00'},
                            {'label': '11:00', 'value': '11:00'},
                            {'label': '12:00', 'value': '12:00'},
                            {'label': '13:00', 'value': '13:00'},
                            {'label': '14:00', 'value': '14:00'},
                            {'label': '15:00', 'value': '15:00'},
                            {'label': '16:00', 'value': '16:00'},
                            {'label': '17:00', 'value': '17:00'},
                            {'label': '18:00', 'value': '18:00'},
                            {'label': '19:00', 'value': '19:00'},
                            {'label': '20:00', 'value': '20:00'},
                            {'label': '21:00', 'value': '21:00'},
                            {'label': '22:00', 'value': '22:00'},
                            {'label': '23:00', 'value': '23:00'}
                        ],
                        value="06:00",
                        style={"width": "80%", "height":"40px", "margin-top":"5px"}
                    )
#Here are constants that are going to be your time pickers in the ui

end_date_picker = dcc.DatePickerSingle(
                    id='end_date_picker',
                    min_date_allowed=datetime.date(2021, 1, 1),
                    max_date_allowed=datetime.date(2024, 12, 31),
                    date=datetime.date.today(),
                    display_format = "DD-MM-YYYY",
                    style={"margin-left": "5px"})
                    
#Here are constants that are going to be your date pickers in the ui


end_time_picker = dcc.Dropdown(
                        id='end_time_picker',
                        options=[
                            {'label': '00:00', 'value': '00:00'},
                            {'label': '01:00', 'value': '01:00'},
                            {'label': '02:00', 'value': '02:00'},
                            {'label': '03:00', 'value': '03:00'},
                            {'label': '04:00', 'value': '04:00'},
                            {'label': '05:00', 'value': '05:00'},
                            {'label': '06:00', 'value': '06:00'},
                            {'label': '07:00', 'value': '07:00'},
                            {'label': '08:00', 'value': '08:00'},
                            {'label': '09:00', 'value': '09:00'},
                            {'label': '10:00', 'value': '10:00'},
                            {'label': '11:00', 'value': '11:00'},
                            {'label': '12:00', 'value': '12:00'},
                            {'label': '13:00', 'value': '13:00'},
                            {'label': '14:00', 'value': '14:00'},
                            {'label': '15:00', 'value': '15:00'},
                            {'label': '16:00', 'value': '16:00'},
                            {'label': '17:00', 'value': '17:00'},
                            {'label': '18:00', 'value': '18:00'},
                            {'label': '19:00', 'value': '19:00'},
                            {'label': '20:00', 'value': '20:00'},
                            {'label': '21:00', 'value': '21:00'},
                            {'label': '22:00', 'value': '22:00'},
                            {'label': '23:00', 'value': '23:00'}
                        ],
                        value="06:00",
                        style={"width": "80%", "height":"40px", "margin-top":"5px"}, #style=dict(display='flex')
                    )
                    
#Here are constants that are going to be your time pickers in the ui

database = dcc.Dropdown(
            id='database',
            options=[
                {'label': 'your db', 'value': 'yourb'},
                {'label': 'your db', 'value': 'your db'},
            ],
            value="ked33",
            style={"width": "80%", "height":"40px", "margin-top":"-5px"}, 

        )
#Here are constants that are going to be your databases in the ui
language = dcc.Dropdown(
    id="language",
    options=[
        {"label": "DE", "value": "DE"},
        {"label": "EN", "value": "EN"},
            ],
            value="DE",
            style={"width": "80%", "height":"40px", "margin-top":"-5px"},
        ) 	


#Constants for language




worker_selection = dcc.Dropdown(
                        id='worker_name',
                        options=[
                            {'label': 'all', 'value': 'all'},
                            {'label': 'Admin', 'value': 'Admin'},
                            {'label': 'Jedi master', 'value': 'Jedi master'},
                            {'label': 'Sith lord', 'value': 'Sith lord'},

                        ],
                        value="all",
                        style={"width": "80%", "height":"40px", "margin-top":"-5px"}, 

                    )

#These are constants regarding the worker names

USERS_FILE = "users.csv"

#Calls the file to read the users


    # SIDEBAR_STYLE: This constant defines the CSS styles for the sidebar of the application. It includes positioning, width, padding, and background color.

    # CONTENT_STYLE: This constant defines the CSS styles for the content area of the application. It includes margins, padding, and text alignment.

    # TEXT_STYLE: This constant defines the CSS styles for text elements in the application. It includes text alignment and color.

    # CARD_TEXT_STYLE: This constant defines the CSS styles for text elements within cards or similar components.

    # start_date_picker: This component is a Dash Date Picker Single element for selecting a start date. It allows users to pick a date from a calendar.

    # start_time_picker: This component is a Dash Dropdown element for selecting a start time. It allows users to pick a time from a list of options.

    # end_date_picker: This component is similar to start_date_picker but is used for selecting an end date.

    # end_time_picker: This component is similar to start_time_picker but is used for selecting an end time.

    # database: This component is a Dash Dropdown element for selecting a database. It allows users to pick a database from a list of options.

    # language: This component is a Dash Dropdown element for selecting a language. It allows users to pick a language from a list of options.

    # worker_selection: This component is a Dash Dropdown element for selecting a worker's name. It allows users to pick a worker's name from a list of options.

    # USERS_FILE: This constant specifies the filename for a CSV file containing user data.