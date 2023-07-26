'''
Object Oriented Programming is an important concept in software development. 
In this complete tutorial, I will learn all about OOP and how to implement it using Python.

Instructional video link: https://www.youtube.com/watch?v=Ej_02ICOIgs
'''

class Item:

    def calculate_total_price(self, x, y):

        return x * y

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
