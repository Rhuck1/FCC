

class Category:

    items = []
    ledger = []
    balance = 0.00

    def __init__(self, name):
        print("Initialization successful")
        # Assign to self object
        self.name = name

        # Actions to execute
        Category.items.append(self)

    def deposit(self, amount, description=""):
        Category.ledger.append({"amount": amount, "description": description})
        Category.balance += float(amount)

    def withdraw(self, amount, description=""):
        if Category.balance + (-amount) > 0:
             Category.ledger.append({"amount": (-amount), "description": description})
             Category.balance += float(-amount)
             return True
        else:
            return False

    def get_balance(self):
        return Category.balance

    def transfer(self):
        pass

    def check_funds(self):
        pass

    def __repr__(self):
        pass




def create_spend_chart(categories):
    pass

cat1 = Category("food")
cat1.deposit(250)
cat1.withdraw(10, "cats")
print(cat1.ledger)
print(cat1.balance)
print(cat1.get_balance())