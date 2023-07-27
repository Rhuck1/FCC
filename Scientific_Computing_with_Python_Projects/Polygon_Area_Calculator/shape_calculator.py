import math


class Rectangle:
    
    def __init__(self, width, height):
        
        # Assign to self object
        self.height = height
        self.width = width
        print('initialization completed')

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        else:
            row = '*' * self.width
            rows = (row + '\n') * self.height
            return rows

    def get_amount_inside(self):
        pass

class Square(Rectangle):
    
    def __init__(self, side):

        super().__init__()        )

        # Assign to self object
        self.side = side

rec1 = Rectangle(5, 4)
print(rec1.height)
print(rec1.width)
print(rec1.get_area())
print(rec1.get_perimeter())
print(rec1.get_diagonal())
print(rec1.get_picture())

rec1.set_width(10)
rec1.set_height(8)

print(rec1.height)
print(rec1.width)
print(rec1.get_area())
print(rec1.get_perimeter())
print(rec1.get_diagonal())
print(rec1.get_picture())

sq1 = Square(4)
print(sq1.height)
print(sq1.width)
print(sq1.get_area())
print(sq1.get_perimeter())
print(sq1.get_diagonal())
print(sq1.get_picture())