

import mysql.connector

# Group name: Puna Poudel / Zachary Brown 
# Assignment: module 10.1
# professor: Chandra Bobba
# due date: 07/14/2024


def display_table(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    print(f"\n-- {table_name} --")
    for row in rows:
        print(row)

# Database connection
config = {
    'user': 'root', 
    'password': 'root',  
    'host': '127.0.0.1',
    'database': 'outland_adventures',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    tables = ["Customers", "Trips", "Guides", "Equipment", "Sales", "Rentals", "Employees", "Supplies", "Bookings", "Locations"]
    for table in tables:
        display_table(cursor, table)

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if db.is_connected():
        cursor.close()
        db.close()
