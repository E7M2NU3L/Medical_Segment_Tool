from mysql import connector

# Database
connect = connector.connect(
    host = "localhost",
    user = "root",
    password = "Emm3nAr0k@1908!"
)

cursor = connect.cursor()

# execute the command
cursor.execute("CREATE DATABASE IF NOT EXISTS MedSegment")

# commit the changes
connect.commit()

# closing the connection
cursor.close()
connect.close()

# display the message
print("Database Connected Succesfully")