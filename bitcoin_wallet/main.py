from bitcoin_wallet.db.database_connection import PostgreSQLConnection
from bitcoin_wallet.config import DatabaseConfig

def test_database_connection(databaseConfig):
    try:
        connection = PostgreSQLConnection(user=DatabaseConfig.DB_USER, password=DatabaseConfig.DB_PASSWORD,
                                          host=DatabaseConfig.DB_HOST, port=DatabaseConfig.DB_PORT, dbname=DatabaseConfig.DB_NAME)

        connection.connection.close()
        print("Conexão com o banco de dados bem-sucedida!")

    except Exception as e:
        print(f"Erro ao conectar-se ao banco de dados: {e}")

if __name__ == "__main__":
    test_database_connection(DatabaseConfig)
