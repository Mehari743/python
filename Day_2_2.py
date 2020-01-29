# python classes

# class Test:
#    name='I am the calls'
#    variable=10
# x=Test()
# y=Test()

# def printName():
#     print( ' I a method of the class')
# print(x)
# print(y)

# print(x.name)
# print(y.name)
# print(x.variable)
# print(y.variable)

# class Test:
#     name='I am the calls'
#     variable=10

#     def printName(self):
#       print( ' I a method of the class')

# x=Test()
# x.printName()

# class Test:
#     name='I am the calls'
#     variable=10

#     def printName(self,age):
#       print( ' I a method of the class')
#       print(age)

# x=Test()
# x.printName(80)


# class Test2:
#   def __init__(self):
#       print('I am the init function')
# y=Test2()

# class Test2:
#   def __init__(self,name):
#       self.name=name
#       print('I am the init function')
# y=Test2('y')
# print(y.name)
# x=Test2('x')
# print(x.name)

# class Dog:
#   scientific_name='canis'
#   def __init__(self,name):
#        self.name=name
# duke=Dog('duke')
# bob=Dog('bob')
# print(duke.scientific_name)
# print(duke.name)
# print(bob.scientific_name)
# print(bob.name)

class Hero:
    def __init__(self,name):
       self.name=name
       self.energy=100

    def eating(self,food):
        if food=='pasta':
            self.energy=self.energy+10
        elif food=='pizza':
            self.energy=self.energy-20
mario=Hero('mario')
print(mario.energy)
mario.eating('pizza')
mario.eating('pasta')
adisu=Hero('adisu')
print(adisu.energy)
adisu.eating('pizza')
adisu.eating('pasta')


class BaseClass:
    def printName(self):
        print('I come from the Base class')
class SubClass(BaseClass):
    pass
a=SubClass()
a.printName()
class BaseClass:
    def printName(self):
        print('I come from the Base class')
class SubClass(BaseClass):
   def printName(self):
       print(' I come from the Sub Class')
a=SubClass()
a.printName()


# class Test:
#     name='I am the calls'
#     variable=10

#     def printName(self,age):
#       print( ' I a method of the class')
#       print(age)

# x=Test()

# class Test2:
#   def __init__(self,name):
#       self.name=name
#       print('I am the init function')
# y=Test2('y')
# print(y.name)
# x=Test2('x')
# print(x.name)


# class BaseClass:
#     def printName(self):
#         print('I come from the Base class')
# class SubClass(BaseClass):
#    def printName(self):
#        print(' I come from the Sub Class')
# a=SubClass()
# a.printName()


#exrciese
# class Employee:
#     def __init__(self,name,paycheck):
#       self.name=name
#       self.paycheck=paycheck
#     def raise_paycheck(self,number):
#       self.paycheck=self.paycheck + (self.paycheck*number)
# mario=Employee('Mario',1000)
# print( mario.name)
# print(mario.paycheck)

# mario.raise_paycheck(0.1)
# print(mario.paycheck)

