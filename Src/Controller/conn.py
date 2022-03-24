import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='crud'
)

cursor = con.cursor()

cursor.execute()
