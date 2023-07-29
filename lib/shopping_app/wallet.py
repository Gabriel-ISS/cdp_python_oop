#from user import User

class Wallet:
    from ownable import set_owner
    def __init__(self, owner):
        self.set_owner(owner)
        self.balance = 0

    def deposit(self, amount: int):
        self.balance += int(amount)

    def withdraw(self, amount: int):
        if not self.balance >= amount:
            return
        self.balance -= int(amount)
        return amount
    
    def transfer_to(self, receiver, amount):
        self.withdraw(amount)
        receiver.wallet.deposit(amount)
