class Category:

    def __init__(self, category):
        # Assign to self object
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        can_withdraw = self.check_funds(amount)

        if can_withdraw:
             self.ledger.append({"amount": (-1.0 * amount), "description": description})

        return can_withdraw

    def get_balance(self):
        tot_balance = float(sum([item['amount'] for item in self.ledger]))
        return tot_balance
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True 

    def transfer(self, amount, budget_category):
        can_transfer = self.check_funds(amount)

        if can_transfer:
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
        
        return can_transfer

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

    names_list = []
    withdraw_list = []
    
    # Formatting names retreived from class instance and placing into list
    for category in categories:
        names = category.category
        names_list.append(names)
        height = len(max(names_list, key=len))
        formatted = [name.ljust(height) for name in names_list]
    
    # Retreiving percentages from class instance spend and placing into list
        withdraw_total = 0
        for item in category.ledger:
            amount = item['amount']
            if amount < 0:
                withdraw_total += amount
        withdraw_list.append(withdraw_total)
    total = int(round(sum(withdraw_list)))

    percentages = []

    for val in withdraw_list:
        per = val * 100 / total
        percent = round(per//10) * 10
        percentages.append(percent)

    bottom_chart_width = 2 * len(categories) + 4

    chart = "Percentage spent by category\n"

    for num in reversed(range(0, 110, 10)):

        chart += f"{num}|".rjust(4)

        for percent in percentages:
            if percent >= num:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    chart += "    " + ("-" * bottom_chart_width) + "\n"

    for row in zip(*formatted):
        chart += "     " + ("  ".join(row)) + "  \n"
    

    return chart.rstrip('\n')



