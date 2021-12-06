#   Name:       Tatiyana Dean
#   Date:       12/6/21
#   Course:     CSD-310
#   Assignment: Module 9.3 PySports Update and Delete

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

cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1);")

cursor.execute(
    "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER INSERT --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print()

cursor.execute(
    "UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

cursor.execute(
    "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER UPDATE --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print()

cursor.execute("DELETE FROM player WHERE first_name = 'Smeagol';")

cursor.execute(
    "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

players = cursor.fetchall()
print("-- DISPLAYING PLAYERS AFTER DELETE --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print()

input("\n\nPress any key to continue... ")

db.close()    