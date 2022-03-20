import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='crud2'
)

cursor = con.cursor()

cursor.execute()
