class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other):
        return Book(self.pages+ other.pages)
b1=Book(100)
b2=Book(200)
b3 = b2 + b2
print(b3.pages)

#employee --overload
def __init__(self,salary):
    self.salary = salary
def __gt__(self,other):
    return self.salary > other.salary
e1 = Employee(50000)
e2 = Employee(30000)

print(e1 > e2)
print(e2 > e1)

#temperature -- overload -
class Temperature:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


t1 = Temperature(35)
t2 = Temperature(20)

print(t1 - t2)

#Rectangle --overload *
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __mul__(self, other):
        area1 = self.length * self.width
        area2 = other.length * other.width
        return area1 * area2


r1 = Rectangle(4, 5)
r2 = Rectangle(2, 3)

print(r1 * r2)

#Time -- overload +
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours

        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes)

    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes"


t1 = Time(2, 40)
t2 = Time(1, 35)

print(t1 + t2)

#shoppingcart
class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices

    def __add__(self, other):
        return ShoppingCart(self.prices + other.prices)

    def __str__(self):
        return str(self.prices)


c1 = ShoppingCart([100, 200])
c2 = ShoppingCart([50, 150])

c3 = c1 + c2
print(c3)
#Distance — Overload +, -, and ==
class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)

    def __sub__(self, other):
        return Distance(self.meters - other.meters)

    def __eq__(self, other):
        return self.meters == other.meters

    def __str__(self):
        return f"{self.meters} meters"


d1 = Distance(50)
d2 = Distance(30)

print(d1 + d2)
print(d1 - d2)
print(d1 == d2)

#Vector — Overload +, -, and *
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)