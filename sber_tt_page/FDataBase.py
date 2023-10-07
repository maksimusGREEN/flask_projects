import sqlite3
 
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
 
    def getPlayers(self):
        sql = '''SELECT * FROM sber_players'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения из БД")
        return []
    
    def clearTable(self):
        try:
            self.__cur.execute("DELETE from sber_players")
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка очистки таблицы в БД "+str(e))
            return False
 
        return True

    def fillTable(self, *args):
        try:
            self.__cur.execute("INSERT INTO sber_players VALUES(?, ?, ?, ?)", tuple(args))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления строки в БД "+str(e))
            return False
 
        return True