import pymysql


class Conection:
    def __init__(self) -> None:
        pass

    def getConection(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='crud'
        )
        return con
