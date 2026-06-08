import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anvi@243",
    database="school_management_system"
)

cursor = conn.cursor()