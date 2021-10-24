try:
    import sqlite3
    import pandas as pd
except Exception as e:
    print(e)

class DataBase:
    def __init__(self, database="data.db", createTable=True):
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.connectionfile = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursorfile = self.connectionfile.cursor()
        if createTable:
            self.createTable()
    
    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data2018 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data2019 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data2020 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data2021 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")

        self.cursorfile.execute("CREATE TABLE IF NOT EXISTS Data2018 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursorfile.execute("CREATE TABLE IF NOT EXISTS Data2019 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursorfile.execute("CREATE TABLE IF NOT EXISTS Data2020 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursorfile.execute("CREATE TABLE IF NOT EXISTS Data2021 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")


    def insertData(self, nome, formacao, titulo, ano):
        if type(titulo) == list:
            for item in titulo:
                self.cursor.execute(f"INSERT INTO Data{ano} (id, primeiro_nome, nome_completo, formacao, titulo, ano) VALUES (?, ?, ?, ?, ?, ?)", (None, nome.split(" ")[0], nome, formacao, item, ano))
        else:
            self.cursor.execute(f"INSERT INTO Data{ano} (id, primeiro_nome, nome_completo, formacao, titulo, ano) VALUES (?, ?, ?, ?, ?, ?)", (None, nome.split(" ")[0], nome, formacao, titulo, ano))
    
    def insertDataFile(self, nome, formacao, titulo, ano):
        if type(titulo) == list:
            for item in titulo:
                self.cursorfile.execute(f"INSERT INTO Data{ano} (id, primeiro_nome, nome_completo, formacao, titulo, ano) VALUES (?, ?, ?, ?, ?, ?)", (None, nome.split(" ")[0], nome, formacao, item, ano))
        else:
            self.cursorfile.execute(f"INSERT INTO Data{ano} (id, primeiro_nome, nome_completo, formacao, titulo, ano) VALUES (?, ?, ?, ?, ?, ?)", (None, nome.split(" ")[0], nome, formacao, titulo, ano))

    def selectData(self, ano):
        query = self.cursorfile.execute(f"SELECT * From Data{ano}")
        cols = [column[0] for column in query.description]
        df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

        df.drop(["id"], axis=1, inplace=True)
        
        df.drop_duplicates(inplace=True)
        df.reset_index(inplace=True)
        df.drop(["index"], axis=1, inplace=True)
        
        return df

    def __selectData(self, ano):
        query = self.cursor.execute(f"SELECT * From Data{ano}")
        cols = [column[0] for column in query.description]
        df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

        df.drop(["id"], axis=1, inplace=True)
        
        df.drop_duplicates(inplace=True)
        df.reset_index(inplace=True)
        df.drop(["index"], axis=1, inplace=True)
        
        return df

    def dellAll(self, ano):
        self.cursorfile.execute(f"DELETE FROM Data{ano}")
        self.connectionfile.commit()
    
    def saveInFile(self, ano):
        df = self.__selectData(ano)
        for i in range(len(df)):
            while True:
                try:
                    self.insertDataFile(df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4])
                    break
                except sqlite3.OperationalError:
                    continue
        self.connectionfile.commit()
