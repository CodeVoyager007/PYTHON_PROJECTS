# 1. Using self 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

# Example
s = Student("Ayesha Mughal", 16)
s.display()


# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# Example
c1 = Counter()
c2 = Counter()
Counter.show_count()


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car started.")

# Example
car = Car("Toyota")
print(car.brand)
car.start()


# 4. Class Variables and Class Methods
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example
b1 = Bank()
b2 = Bank()
print(b1.bank_name)  # ABC Bank
Bank.change_bank_name("XYZ Bank")
print(b2.bank_name)  # XYZ Bank


# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example
print(MathUtils.add(5, 3))


# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Example
l = Logger()
del l


# 7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # public
        self._salary = salary       # protected
        self.__ssn = ssn            # private

# Example
emp = Employee("Ayesha", 50000, "123-45-6789")
print(emp.name)         # Accessible: Ayesha
print(emp._salary)      # Accessible (protected): 50000
try:
    print(emp.__ssn)    # Raises AttributeError
except AttributeError:
    print("Cannot access private __ssn directly")
print(emp._Employee__ssn)  # Accessible via name : 123-45-6789


# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Example
t = Teacher("Mr. Smith", "Math")
print(t.name, t.subject)

# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

# Example
r = Rectangle(4, 5)
print(r.area())


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Example
d = Dog("Buddy", "Labrador")
d.bark()


# 11. Class Methods
class Book:
    total_books = 0

    def __init__(self):
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
# Example
b1 = Book()
b2 = Book()
print(Book.total_books)


# 12.Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example
print(TemperatureConverter.celsius_to_fahrenheit(0))


# 13. Composition
class Engine:
    def start(self):
        print("Engine started.")

class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

# Example
eng = Engine()
car = CarWithEngine(eng)
car.start_engine()


# 14. Aggregation
class EmployeeAgg:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

# Example
emp = EmployeeAgg("Alice")
dept = Department("HR", emp)
print(dept.employee.name)


# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Example
d = D()
d.show()  # Output: B (MRO: D, B, C, A)


# 16. Function Decorators
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Example
say_hello()


# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

# Example
p = Person()
print(p.greet())


# 18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example
prod = Product(100)
print(prod.price)
prod.price = 200
print(prod.price)
del prod.price


# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example
m = Multiplier(3)
print(callable(m))  # True
print(m(10))        # 30


# 20.Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

# Example
try:
    check_age(15)
except InvalidAgeError as e:
    print(e)


#21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Example
for i in Countdown(5):
    print(i)