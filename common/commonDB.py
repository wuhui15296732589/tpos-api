import pymysql
from testFile import readConfig as readConfig
from common.Log import MyLog as Log
log = Log.get_log()
logger = log.logger
localReadConfig = readConfig.ReadConfig()

class MyDB:
    global host, username, password, port, database, config
    host = localReadConfig.get_db("host")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):

        self.logger = logger
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")



if __name__ == '__main__':
    mydb = MyDB()
    st = mydb.executeSQL('SELECT customer_id FROM t_pos')
    ss = mydb.get_all(st)
    print(ss)

