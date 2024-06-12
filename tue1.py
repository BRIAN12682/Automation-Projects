class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof! and I am {self.age} years old ")

my_dog = Dog("Rex", 5)
my_dog.bark()

#pip install matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Plot')
plt.show()

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

for value in my_generator():
    print(value)