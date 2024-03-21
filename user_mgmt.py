import csv
import constants



def read_users():
    with open(constants.USERS_FILE, mode="r") as infile:
        reader = csv.reader(infile, delimiter=";")
        #Skip the first line
        next(reader, None)
        #Load user password pairs in to disctionary
        users= {row[0]:row[1] for row in reader}
    #print(users)
    return users




read_users()

#This script is for reading the csv and letting the data being used for log in

