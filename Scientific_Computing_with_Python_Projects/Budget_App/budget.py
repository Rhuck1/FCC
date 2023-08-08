class Category:

    def __init__(self, category):
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
        if self.withdraw(amount, f"Transer to {budget_category.category}"):
            return False
        else:
            budget_category.deposit(amount, f"Transfer from {budget_category.category}")
            return True

    def __repr__(self):
        total = f"Total: " + f"{self.get_balance():.2f}"
        header = f"{self.category:*^30}\n"
        ledger = ""
        for item in self.ledger:
            description = f"{item['description']:<23}" 
            amount = f"{item['amount']:>7.2f}"
            ledger += f"{description[:23]}{amount[:7]}\n"

        return header + ledger + total

def create_spend_chart(categories):

    chart = "Percentage spent by category\n"

    height = len(max(categories, key=len))
    formatted_categories = [names.ljust(height) for names in categories]

    percentages = [10, 70, 30]

    bottom_chart_width = 2 * len(categories) + 4
    
    

    for num in reversed(range(0, 110, 10)):

        chart += f"{num}|".rjust(5)

        for percent in percentages:
            if percent >= num:
                chart += " o "
            else:
                chart += "   "

        chart += "\n"


    chart += ("-" * bottom_chart_width + "\n").ljust(bottom_chart_width + 5)

    for name in zip(*formatted_categories):
        chart += " " + ("  ".join(name) + "\n").rjust(bottom_chart_width)

    

    return chart



