'''
Object Oriented Programming is an important concept in software development. 
In this complete tutorial, I will learn all about OOP and how to implement it using Python.

Instructional video link: https://www.youtube.com/watch?v=Ej_02ICOIgs
'''
import csv


class Item:

    pay_rate = 0.8 # The pay rate after 20% discount

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):

        return self.price * self.quantity
    
    def apply_discount(self):

        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):

        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero (i.e. 5.0, 10.0)
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    

class Phone(Item):

    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):

        # Call to super function to have access to all attribures & methods
        # This call to super replaces the need for rewriting assertions and self
        # assignments that already exist in parent class Item
        super().__init__(
            name, price, quantity
        )
        
        # Run validations to the received arguments
        # assert price >= 0, f"Price {price} is not greater than or equal to zero"
        # assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev10", 700, 5, 1)