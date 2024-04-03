from flask import Flask

app = Flask(__name__)

bank = {}

@app.route('/<account_id>', methods=['GET'])
def get_balance(account_id: str):

    if account_id in bank:
        return {"balance": bank[account_id]}, 200

    return 'Account not found', 404

@app.route('/<account_id>/<float:deposit_value>', methods=['PUT'])
def deposit(account_id: str, deposit_value: str):
    if account_id in bank:
        bank[account_id] += deposit_value
        return {"balance": bank[account_id]}, 200

    return 'Account not found', 404

@app.route('/<account_id>/<float:withdraw_value>', methods=['PATCH'])
def withdraw(account_id: str, withdraw_value: float):
    if account_id in bank:

        if bank[account_id] < withdraw_value:
            return 'Insufficient funds', 400
        
        bank[account_id] -= withdraw_value
        return {"balance": bank[account_id]}, 200

    return 'Account not found', 404

@app.route('/<account_id>', methods=['POST'])
def create_account(account_id: str):

    if account_id in bank:
        return 'Account already exists', 400

    bank[account_id] = 0
    return 'Account created', 201

