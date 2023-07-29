

class Category:

    items = []
    ledger = []

    def __init__(self, name):
        print("Initialization successful")
        # Assign to self object
        self.name = name

        # Actions to execute
        Category.items.append(self)

    def deposit(self, amount, description=" "):
        ledger.append({"amount": amount, "description": description})

    def withdraw(self):
        pass

    def get_balance(self):
        pass

    def transfer(self):
        pass

    def check_funds(self):
        pass

    def __repr__(self):
        pass




def create_spend_chart(categories):
    pass

cat1 = Category("food")
print(Category.all)