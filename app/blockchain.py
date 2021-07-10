import uuid

class Block:
    def __init__(self, transactions: list=[], previous_hash: str):
        self.id = uuid.uuid4()
        self.transactions = transactions
        self.previous_hash = previous_hash

class Blockchain:
    def __init__(self):
        self.unconfirmated_chain = []
        self.chain = []
