import urllib
import urllib.parse
import sqlalchemy
import pandas as pd


class Database_connection:
    def __init__(self, server, database, driver):
        self.server = server
        self.driver = driver
        self.database = database

    def create_engine(self):
        connection_string = """DRIVER={%s};
                            Server={%s};
                            DATABASE=%s;
                            UID=%s;
                            PWD=%s;""".format(self.driver, self.database, "***", "***")
        # replacing special characters so the string can be safely included in a URL query string. It also replaces spaces with +, which is useful for encoding form data
        params = urllib.parse.quote_plus(connection_string)
        self.engine = sqlalchemy.create_engine(
            'mssql:///?odbc_connect{}'.format(params))
        
    def create_connection(self):
        self.engine.connect()


class SQL_operations:
    def __init__(self, database, schema, DataFrame, table_name, engine):
        self.database = database
        self.schema = schema
        self.DataFrame = DataFrame
        self.table_name = table_name
        self.engine = engine

    def truncate_table(self):
        # truncate table => quickly delete all rows from a table, while keeping the structure of the table intact.
        truncate_query = 'TRUNCATE TABLE {database}.{schema}.{table}'.format(database=self.database,
                                                                             schema=self.schema,
                                                                             table=self.table_name)
        with self.engine.connect() as cursor:
            cursor.execution_options(autocommit=True).execute(truncate_query)

    def check_if_table_exists(self):
        return self.engine.has_table(table_name=self.table_name, schema=self.schema)
    
    def create_table_skeleton(self):
        '''
        create a table in a SQL database with the correct schema but no real data, using just the structure of a Pandas DataFrame
        ''' 
        # Gets the first row of the DataFrame. This ensures you retain the structure (columns and data types) but minimize data being written
        head = self.DataFrame.head(1)
        head.to_sql(name=self.table_name,
                    con=self.engine,
                    schema=self.schema,
                    index=False,
                    if_exists='replace')
        
    def insert_data(self, customType=None):
        self.DataFrame.to_sql(name=self.table_name,
                              con=self.engine,
                              schema=self.schema,
                              index=False,
                              if_exists='append',
                              dtype=customType)
        
    def upload_with_method(self, method="append", customType=None):
        self.DataFrame.to_sql(name=self.table_name,
                              con=self.engine,
                              schema=self.schema,
                              index=False,
                              if_exists=method,
                              dtype=customType)
        
    