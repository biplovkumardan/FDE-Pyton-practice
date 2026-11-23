import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='company_db'
)

print("Database connection established successfully!")

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()

for employee in employees:
    print(employee)

cursor.close()
conn.close()