class Category:

    def __init__(self, category):
        print("Initialization successful")
        # Assign to self object
        self.category = category
        self.ledger = []
        self.balance = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += float(amount)

    def withdraw(self, amount, description=""):
        if self.balance + (-1.0 * amount) > 0:
             self.ledger.append({"amount": (-1.0 * amount), "description": description})
             self.balance += float(-1.0 * amount)
             return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if amount > self.get_balance(self):
            return False
        else:
            self.withdraw(amount, f"Transfer to {category}")
            self.deposit(amount, f"Transfer from {}")

    def check_funds(self):
        pass

    def __repr__(self):
        pass




def create_spend_chart(categories):
    pass



cat1 = Category("food")
cat1.deposit(250)
print(cat1.withdraw(300, "cats"))
print(cat1.get_balance())