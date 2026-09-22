#type()
a = 10
b = 5.6
c = "Hello"
d = [1, 2, 3, 4, 5, 4]
e = (1, 2, 3, 4, 5)
f = {1, 2, 3, 4, 5}
g = {"name": "Sanjana"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
'''
isinstance(): to check if the value/ object belongs to a particular class or not. It returns True if the object belongs to the specified class, otherwise it returns False.
syntax:
isinstance(object, type)
it gives us boolean value True or False.
'''
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, str))
print(isinstance(d, list))
print(isinstance(e, tuple))
print(isinstance(f, set))
print(isinstance(g, dict))

#Duck Typing: same method acts as same behaviour 
class Dog:
    def sound(self):
        print("Bow - Bow")
class Cat:
    def sound(self):
        print("Meow - Meow")
def make_sound(animal):
    animal.sound()
d = Dog()
c = Cat()
make_sound(d)
make_sound(c)

def process(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, float):
        return data + 10.5
print(process(10))        # Output: 10
print(process("sanjana"))  # Output: SANJANA 
print(process(5.5))      # Output: 16.0

#Interview Question 
class A:
    pass
class B(A):
    pass
obj = B()
print(type(obj) == B)  # Output: True
print(type(obj) == A)  # Output: False

print(isinstance(obj, B))  # Output: True
print(isinstance(obj, A))  # Output: True    