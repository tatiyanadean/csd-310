#   Name:       Tatiyana Dean
#   Date:       12/1/21
#   Course:     CSD-310
#   Assignment: Module 8.3 PySports Table Queries

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "user",
    "password": "Everythinghaschanged27",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()
print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}".format(team[2]))
    print()
print()

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

players = cursor.fetchall()
print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print()

input("\n\nPress any key to continue... ")

db.close()    