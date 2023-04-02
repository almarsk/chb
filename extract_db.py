import sqlite3

# Connect to the database file
conn = sqlite3.connect('chatbot.db')

# Create a cursor object to execute SQL queries
cursor_users = conn.cursor()

# Execute a simple query to retrieve all rows from a table
cursor_users.execute("SELECT * FROM user WHERE nick LIKE '%b%'")

# Fetch all the rows and print them
rows = cursor_users.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection objects
cursor_users.close()
conn.close()
