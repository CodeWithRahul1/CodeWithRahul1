Encapsulation (Data Hiding)
Polymorphism (Many Forms)
Duck Typing
mixin


'''Duck Typing'''

'''
✅ Duck Typing Definition (for Interview)
Duck typing is a programming concept used in dynamically typed languages like Python, where the type or class of an object is less important than the methods and properties that the object defines. In other words, an object’s suitability for use is determined by whether it "behaves like" the expected type, rather than whether it is that type.

This concept comes from the phrase:

“If it looks like a duck, swims like a duck, and quacks like a duck — then it probably is a duck.”

In Python, this allows functions and classes to operate on any object that implements the required behavior (methods/attributes), enabling flexible and polymorphic code without requiring inheritance or explicit interfaces.'''

#example

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    # Duck typing in action
    thing.quack()

duck = Duck()
person = Person()

make_it_quack(duck)   # Output: Quack!
make_it_quack(person) # Output: I'm pretending to be a duck!
