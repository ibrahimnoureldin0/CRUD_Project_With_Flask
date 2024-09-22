# Import libraries
from flask import Flask, request, render_template, redirect, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route("/add", methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'GET':
        return render_template("form.html")
    if request.method == 'POST':
        transation = {
            'id': len(transactions)+1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transation)
        return redirect(url_for("get_transactions"))
  
# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'GET':
        for trans in transactions:
            if trans['id'] == transaction_id:
                return render_template("edit.html", transaction=trans)
    
    if request.method == 'POST':

        for trans in transactions:
            if trans['id'] == transaction_id:
                trans['date'] = request.form['date']
                trans['amount'] = float(request.form['amount'])
                break

        return redirect(url_for("get_transactions"))
    
    return {"message": "Transaction not found"}, 404

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for trans in transactions:
        if trans['id'] == transaction_id:
            transactions.remove(trans)
            break
    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=6060)
    