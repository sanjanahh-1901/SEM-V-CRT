#Single Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

#Multiple Inheritance
class Parent1:
    def func1(self):
        print("This function is in parent 1 class.")
        
class Parent2:
    def func2(self):
        print("This function is in parent 2 class.")

class Child(Parent1, Parent2):
    def func3(self):
        print("This function is in child class.")

#Multilevel Inheritance
class GrandParent:
    def func1(self):
        print("This function is in grandparent class.")

class Parent(GrandParent):
    def func2(self):
        print("This function is in parent class.")      

class Child(Parent):
    def func3(self):
        print("This function is in child class.")

#Hierarchical Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child1(Parent):
    def func2(self):
        print("This function is in child 1 class.")

class Child2(Parent):
    def func3(self):
        print("This function is in child 2 class.")

#Hybrid Inheritance:
class Parent1:
    def func1(self):
        print("This function is in parent 1 class.")

class Parent2:
    def func2(self):
        print("This function is in parent 2 class.")

class Child(Parent1, Parent2):
    def func3(self):
        print("This function is in child class.")

        