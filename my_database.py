import mysql.connector

dataBase = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='Alinathani.201'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE crmdatabase")  # avoid adding ' or " here in the name

print("Database built successfully")

# just need to do this once to build the database
