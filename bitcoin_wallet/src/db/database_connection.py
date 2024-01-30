import psycopg2
from bitcoin_wallet.config import DatabaseConfig

class Session:
    def __init__(self, user=DatabaseConfig.DB_USER, password=DatabaseConfig.DB_PASSWORD,
                 host=DatabaseConfig.DB_HOST, port=DatabaseConfig.DB_PORT, dbName=DatabaseConfig.DB_NAME):
        self.connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            dbname=dbName
        )

    def execute_query(self, query, parameters=None):
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
        return cursor

