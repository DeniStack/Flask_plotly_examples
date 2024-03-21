import mssql_conn

#for app_users.py
def build_db_query_string_app1():
    db_query_string = """SELECT LoginLog.Timestamp, LoginLog.ChipID, LoginLog.WorkerName, LoginLog.UserLvl 
                         FROM LoginLog 
                         WHERE LoginLog.Timestamp #BETWEEN ? AND ?""" 
    return db_query_string

#BETWEEN ? AND ?""" means the date and time picker