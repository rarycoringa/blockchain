import uuid

from typing import List

class Wallet:
    def __init__(self, label: str = None, current_balance: float = 0.0):
        self.id = uuid.uuid4()
        self.label = label
        self.current_balance = current_balance

    def deposit(self, amount: float) -> dict:
        self.current_balance += amount
        result, message = 'success', None

        return {'result': result, 'message': message}

    def withdraw(self, amount: float) -> dict:
        if self.current_balance >= amount:
            self.current_balance -= amount
            result, message = 'success', None
        else:
            result, message = 'error', 'insufficient funds'

        return {'result': result, 'message': message}

class Transaction:
    def __init__(self, from_wallet: Wallet, to_wallet: Wallet, amount: float):
        self.id = uuid.uuid4()
        self.from_wallet = from_wallet
        self.to_wallet = to_wallet
        self.amount = amount

    def commit(self) -> dict:
        withdraw_result = self.from_wallet.withdraw(self.amount)

        if withdraw_result['result'] == 'success':
            deposit_result = self.to_wallet.deposit(self.amount)

            result, message = 'success', None
        else:
            result, message = 'error', f'insufficient funds in wallet with ID started with {str(self.from_wallet.id)[:8]}'

        return {'result': result, 'message': message}
