import MySQLdb
try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="test1234")
    print("Connection successful with password 'test1234'")
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    for row in cursor.fetchall():
        print(row)
    db.close()
except Exception as e:
    print(f"Failed with password 'test1234': {e}")

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="")
    print("Connection successful with empty password")
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")
    for row in cursor.fetchall():
        print(row)
    db.close()
except Exception as e:
    print(f"Failed with empty password: {e}")
