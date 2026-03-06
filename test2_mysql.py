import mysql.connector
import sys
print("Before connect", flush=True)
try:
    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="")
except Exception as e:
    print("Caught:", e)
print("After connect", flush=True)
