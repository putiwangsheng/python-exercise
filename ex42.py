class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name):
        self.name = name
        print(name)

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        # 调用父类的__init__方法
        super(Employee, self).__init__(name)
        self.salary = salary

rover = Dog("Rover")
frank = Employee("Frank", 120000)
frank.pet = rover
