class Category:

    def __init__(self, category):
        print("Initialization successful")
        # Assign to self object
        self.category = category
        self.ledger = []
        self.balance = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.balance + (-1.0 * amount) > 0:
             self.ledger.append({"amount": (-1.0 * amount), "description": description})
             self.balance += (-1.0 * amount)
             return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
    def check_funds(self, amount):
        if amount >= self.get_balance():
            return False
        else:
            return True 

    def transfer(self, amount, category_selection):
        if amount > self.get_balance():
            return False
        else:
            self.withdraw(amount, f"Transfer to {category_selection.category}")
            self.deposit(amount, f"Transfer from {category_selection.self.category}")
            return True

    def __repr__(self):

        return f""


def create_spend_chart(categories):
    pass


cat1 = Category("food")
cat2 = Category("entertainment")

cat1.deposit(250)
cat2.deposit(1000)

print(cat1.withdraw(300, "cats"))
print(cat2.withdraw(20, "turkey meatz"))

print(cat1.get_balance())
print(cat2.get_balance())

print(cat2.transfer(200, "food"))

print(cat1.get_balance())
print(cat2.get_balance())

cat1.transfer(100, 'clothing')

print(cat1.check_funds(260))

print(cat1.ledger)
