# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
r = float(input("Enter the radius of the circle: "))
circle = Circle(r)
print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())

# Create a class Book that stores details like the title, author, and price of a book. Add methods to display the details of the book and apply a discount to the price. (a) Create two objects for different books and display their details. (b) Apply a 10% discount to one of the books and display the updated price.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount

book1 = Book("Python Programming", "John Smith", 550)
book2 = Book("Data Structures in C++", "Mark Johnson", 650)

print("Before Discount:")
book1.display_details()
book2.display_details()

book2.apply_discount(10)

print("After 10% Discount on Book 2:")
book2.display_details()