from bitcoin_wallet.model import BitcoinTransaction
from bitcoin_wallet.db.database_connection import Session
import logging

class BitcoinTransactionRepository:
    def __init__(self):
        self.connection = Session()
        self.create_transactions_table()

    def create_transactions_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS bitcoin_transactions (
                id SERIAL PRIMARY KEY,
                coin_name CHAR(255),
                purchase_date TIMESTAMP,
                purchase_price REAL
            )
        '''
        self.connection.execute_query(query)
        self.connection.connection.commit()

    def save_transaction(self, coin_name, purchase_date, purchase_price):
        query = '''
            INSERT INTO bitcoin_transactions (coin_name, purchase_date, purchase_price)
            VALUES (%s, %s, %s)
        '''
        parameters = (coin_name, purchase_date, purchase_price)

        try:
            self.connection.execute_query(query, parameters)
            self.connection.connection.commit()
            logging.info("Inserção bem-sucedida no banco de dados.")
        except Exception as e:
            logging.error(f"Falha na inserção no banco de dados: {str(e)}")
            self.connection.connection.rollback()

    def get_transactions(self):
        query = "SELECT id, coin_name, purchase_date, purchase_price FROM bitcoin_transactions"
        cursor = self.connection.execute_query(query)
        records = cursor.fetchall()

        transactions = []
        for record in records:
            transaction = BitcoinTransaction(
                id=record[0],
                coin_name=str(record[1]).strip(),
                purchase_date=record[2],
                purchase_price=record[3]
            )
            transactions.append(transaction)

        return transactions

    def delete_transaction(self, transaction_id):
        query = "DELETE FROM bitcoin_transactions WHERE id = %s"
        parameters = (transaction_id,)

        try:
            self.connection.execute_query(query, parameters)
            self.connection.connection.commit()
            logging.info("Exclusão bem-sucedida no banco de dados.")
        except Exception as e:
            logging.error(f"Falha na exclusão no banco de dados: {str(e)}")
            self.connection.connection.rollback()

