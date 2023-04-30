class Person:
    def __init__(self, name, age, height):
        self.name = name 
        self.age = age
        self.height = height
    
    def __str__(self):
        return str(self.name) + '-> '+ str(self.age) + "---------- " +str(self.height)
    
new = Person("Markis", 23, 5)
print(new.age)
print(new)



