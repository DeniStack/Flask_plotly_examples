import pyodbc

# Define your MSSQL server connection parameters
server = 'your_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'

# Establish a connection to the MSSQL server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the SQL query to create a table for sales data
create_table_query = """
CREATE TABLE Sales (
    SaleDate DATE,
    Game NVARCHAR(50),
    TotalSales INT
)
"""

# Execute the create table query
cursor.execute(create_table_query)
conn.commit()

# Define the SQL query to insert mockup sales data into the table
insert_data_query = """
INSERT INTO Sales (SaleDate, Game, TotalSales)
VALUES
    ('2019-01-01', 'Fortnite', 500),
    ('2019-01-01', 'Minecraft', 700),
    ('2020-01-01', 'Fortnite', 600),
    ('2020-01-01', 'Minecraft', 800),
    ('2021-01-01', 'Fortnite', 900)
"""

# Execute the insert data query
cursor.execute(insert_data_query)
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Database table created and mockup data inserted successfully.")
