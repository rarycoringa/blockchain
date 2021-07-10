import uuid

class User:
    def __init__(self, name: str, balance: float=10.0):
        self.id = uuid.uuid4()
        self.name = name
        self.balance = balance

class Transaction:
    def __init__(self, from: User, to: User, amount: float):
        self.id = uuid.uuid4()
        self.from = from
        self.to = to
        self.amount = amount
