from flask import Flask, render_template, request, redirect, url_for
from bitcoin_wallet.src.db.repository import BitcoinTransactionRepository
import os

app = Flask(__name__)

transaction_repository = BitcoinTransactionRepository()

app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates')

@app.route('/')
def show_transactions():
    transactions = transaction_repository.get_transactions()
    return render_template('transactions.html', transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    if request.method == 'POST':
        coin_name = request.form['coin_name']
        purchase_date = request.form['purchase_date']
        purchase_price = request.form['purchase_price']

        try:
            new_transaction = {
                "coin_name": coin_name,
                "purchase_date": purchase_date,
                "purchase_price": float(purchase_price)
            }

            transaction_repository.save_transaction(**new_transaction)

            return redirect(url_for('show_transactions'))

        except Exception as e:
            return f"Erro ao conectar-se ao banco de dados: {e}"

@app.route('/delete_transaction/<int:transaction_id>', methods=['GET'])
def delete_transaction(transaction_id):
    try:
        transaction_repository.delete_transaction(transaction_id)
        return redirect(url_for('show_transactions'))

    except Exception as e:
        return f"Erro ao excluir a transação: {e}"

if __name__ == '__main__':
    app.run(debug=True)
