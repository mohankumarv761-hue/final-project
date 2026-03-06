import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mohan@2006',
    'database': 'hospital_management'
}

try:
    print("Connecting...")
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Connected.")
except Exception as e:
    print(f"Error: {e}")
