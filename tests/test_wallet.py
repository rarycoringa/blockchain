import pytest
import uuid

from app.wallet import Wallet, Transaction

class TestWallet:
    def test_wallet_object(self):
        wallet_1 = Wallet('Wallet 1')

        assert isinstance(wallet_1.id, uuid.UUID)
        assert wallet_1.label == 'Wallet 1'
        assert wallet_1.current_balance == 0.0

        wallet_2 = Wallet()

        assert wallet_2.label is None

    def test_wallet_deposit(self):
        amount = 1.25

        wallet = Wallet()

        res = wallet.deposit(amount)

        assert res['result'] == 'success'
        assert res['message'] is None
        assert wallet.current_balance == amount

        res = wallet.deposit(amount)

        assert res['result'] == 'success'
        assert res['message'] is None
        assert wallet.current_balance == amount*2

    def test_wallet_withdraw(self):
        amount = 1.50

        wallet = Wallet()

        res = wallet.deposit(amount)
        res = wallet.withdraw(amount/2)

        assert res['result'] == 'success'
        assert res['message'] is None
        assert wallet.current_balance == amount/2

        res = wallet.withdraw(amount)

        assert res['result'] == 'error'
        assert res['message'] == 'insufficient funds'
        assert wallet.current_balance == amount/2

class TestTransaction:
    def test_transaction_object(self):
        amount_transaction = 5.0

        wallet_1 = Wallet()
        wallet_2 = Wallet()

        transaction = Transaction(wallet_1, wallet_2, amount_transaction)

        assert isinstance(transaction.id, uuid.UUID)
        assert isinstance(transaction.from_wallet, Wallet)
        assert isinstance(transaction.to_wallet, Wallet)
        assert transaction.from_wallet == wallet_1
        assert transaction.to_wallet == wallet_2
        assert transaction.amount == amount_transaction

    def test_transaction_commit(self):
        initial_balance = 10.0
        amount_transaction = 5.0

        wallet_1 = Wallet(current_balance = initial_balance)
        wallet_2 = Wallet(current_balance = initial_balance)

        transaction = Transaction(wallet_1, wallet_2, amount_transaction)

        res = transaction.commit()

        assert res['result'] == 'success'
        assert res['message'] is None

        transaction = Transaction(wallet_1, wallet_2, amount_transaction*2)

        res = transaction.commit()

        assert res['result'] == 'error'
        assert res['message'] is not None
        assert 'insufficient funds in wallet with ID started with ' in res['message']
        assert res['message'][-8:] == str(wallet_1.id)[:8]
