try:
    import sqlite3
    import pandas as pd
except Exception as e:
    print(e)

class DataBase:
    """
    
    Classe para a criação e manipulação de um banco de dados com a biblioteca SQLite
    
    """
    def __init__(self, database="data.db"):
        """
        
        Args:
            database [string] : local do arquivo de dados, caso o arquivo seja inexistente, o mesmo será criado.
                      padrão: data.db
            

        """
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.connectionfile = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursorfile = self.connectionfile.cursor()
        self.__createTable()
    
    def __createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data2018 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data2019 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data2020 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data2021 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")

        self.cursorfile.execute("CREATE TABLE IF NOT EXISTS Data2018 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursorfile.execute("CREATE TABLE IF NOT EXISTS Data2019 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursorfile.execute("CREATE TABLE IF NOT EXISTS Data2020 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")
        self.cursorfile.execute("CREATE TABLE IF NOT EXISTS Data2021 (id INTEGER PRIMARY KEY, primeiro_nome text, nome_completo text, formacao text, titulo text, ano text)")


    def insertData(self, nome, formacao, titulo, ano):
        """

        Inserção de dados na base criada na memória.

        Args:
            nome [string] : nome do autor do artigo
            formacao [string] : nível de formação acadêmica
            titulo [string] : título do artigo
            ano [string/int] : ano de publicação do artigo

        """
        if type(titulo) == list:
            for item in titulo:
                self.cursor.execute(f"INSERT INTO Data{ano} (id, primeiro_nome, nome_completo, formacao, titulo, ano) VALUES (?, ?, ?, ?, ?, ?)", (None, nome.split(" ")[0], nome, formacao, item, ano))
        else:
            self.cursor.execute(f"INSERT INTO Data{ano} (id, primeiro_nome, nome_completo, formacao, titulo, ano) VALUES (?, ?, ?, ?, ?, ?)", (None, nome.split(" ")[0], nome, formacao, titulo, ano))
    
    def insertDataFile(self, nome, formacao, titulo, ano):
        """

        Inserção de dados no arquivo fisíco.

        Args:
            nome [string] : nome do autor 
            formacao [string] : nível de formação do autor 
            titulo [string] : titulo do artigo
            ano [string/int] : ano do artigo
            
        """
        if type(titulo) == list:
            for item in titulo:
                self.cursorfile.execute(f"INSERT INTO Data{ano} (id, primeiro_nome, nome_completo, formacao, titulo, ano) VALUES (?, ?, ?, ?, ?, ?)", (None, nome.split(" ")[0], nome, formacao, item, ano))
        else:
            self.cursorfile.execute(f"INSERT INTO Data{ano} (id, primeiro_nome, nome_completo, formacao, titulo, ano) VALUES (?, ?, ?, ?, ?, ?)", (None, nome.split(" ")[0], nome, formacao, titulo, ano))

    def selectData(self, ano):
        """

        Seleção dos dados a partir do ano na base de dados fisíca.

        Args:
            ano [string/int] : ano de publicação do artigo
        
        Return [DataFrame Pandas] :
            DataFrame pandas com os dados da tabela referente ao ano.

        """
        query = self.cursorfile.execute(f"SELECT * From Data{ano}")
        cols = [column[0] for column in query.description]
        df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

        df.drop(["id"], axis=1, inplace=True)
        
        df.drop_duplicates(inplace=True)
        df.reset_index(inplace=True)
        df.drop(["index"], axis=1, inplace=True)
        
        return df

    def __selectData(self, ano):
        """
        
        Seleção de dados a partir da base de dados na memória.
        
        Args:
            ano [string/int] : ano da publicação de um artigo
        
        Return [DataFrame Pandas] :
            DataFrame pandas com os dados da tabela referente ao ano.

        """
        query = self.cursor.execute(f"SELECT * From Data{ano}")
        cols = [column[0] for column in query.description]
        df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)

        df.drop(["id"], axis=1, inplace=True)
        
        df.drop_duplicates(inplace=True)
        df.reset_index(inplace=True)
        df.drop(["index"], axis=1, inplace=True)
        
        return df

    def dellAll(self, ano):
        """
        
        Deleta toda a tabela de dados de um ano.

        Args:
            ano [string/int] : ano da publicação de um artigo

        """
        self.cursorfile.execute(f"DELETE FROM Data{ano}")
        self.connectionfile.commit()
    
    def saveInFile(self, ano):
        """
        
        Salva os dados da memória em um arquivo fisíco.

        Args:
            ano [string/ano] : ano da publicação de um artigo

        """
        df = self.__selectData(ano)
        for i in range(len(df)):
            while True:
                try:
                    self.insertDataFile(df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4])
                    break
                except sqlite3.OperationalError:
                    continue
        self.connectionfile.commit()
        
    def merge(self, data):
        """
        
        Junta duas base de dados fisicas.

        Args:
            data [string/SQLite] : base de dados a ser adicionada.

        """
        connec = sqlite3.connect(data)
        cursor = connec.cursor()
        anos = [2018,2019,2020,2021]
        for ano in anos:
            for i, _, nome_completo, formacao, titulo, ano in cursor.execute(f"SELECT * From Data{ano}"):
                self.insertDataFile(nome_completo, formacao, titulo, ano)
        self.connectionfile.commit()
