class Category:

    def __init__(self, category):
        print("Initialization successful")
        # Assign to self object
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.get_balance() >= amount:
             self.ledger.append({"amount": (-1.0 * amount), "description": description})
             return True
        else:
            return False

    def get_balance(self):
        tot_balance = float(sum([item['amount'] for item in self.ledger]))
        return tot_balance
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True 

    def transfer(self, amount, budget_category):
        if amount > self.get_balance():
            return False
        else:
            self.withdraw(amount, "Transfer to " + category.category)
            self.deposit(amount, f"Transfer from " + self.category)
            return True

    def __repr__(self):
        title_line = self.category.center(30, "*")
        
        return title_line


def create_spend_chart(categories):
    pass


cat1 = Category("food")
cat2 = Category("entertainment")

cat1.deposit(250)
cat2.deposit(1000)

print(cat1.get_balance())
print(cat2.get_balance())
print(cat1.check_funds(260))

# print(cat2.transfer(200, "food"))

# print(cat1.get_balance())
# print(cat2.get_balance())

# cat1.transfer(100, 'clothing')



# print(cat1.withdraw(300, "cats"))
# print(cat2.withdraw(20, "turkey meatz"))

# print(cat1)

