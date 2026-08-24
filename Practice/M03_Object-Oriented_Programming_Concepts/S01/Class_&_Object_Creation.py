class Example:
    x = 1000 #data -- class variable
    def display(self):
        print("This is an Example class display method")

obj = Example() #object creation
print(obj.x) #accessing class variable using object
obj.display() #accessing class method using object

'''
Create class circle with 2 methods:
1. area() - to calculate area of circle
2. perimeter() - to calculate perimeter of circle
'''

from math import pi

class Circle:
    r = 7
    def area(self):
        return pi * self.r * self.r

    def perimeter(self):
        return 2 * pi * self.r

c = Circle()
print("Area of circle:", c.area())
print("Perimeter of circle:", c.perimeter())

#Create no. of objects created for Circle class
class A:
    count = 0
    def __init__(self):
        A.count += 1

c1 = A()
c2 = A()
c3 = A()
print(c.area())
print(c.perimeter())
print(c1.area())
print(c1.perimeter())
print(c2.area())
print(c2.perimeter())
print(c3.area())
print(c3.perimeter())
print("No. of objects created for class A:", A.count)

#Leetcode 1603. Design Parking System
#Traditional Approach
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small   

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
        return False
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

#Optimized Approach
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType - 1] > 0:
            self.slots[carType - 1] -= 1
            return True
        return False