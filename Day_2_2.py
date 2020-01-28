# python classes
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


#exriese

class Employee:
    def __init__(self,name,paycheck):
      self.name=name
      self.paycheck=paycheck
    def raise_paycheck(self,number):
      self.paycheck=self.paycheck + (self.paycheck*number)
mario=Employee('Mario',1000)
print( mario.name)
print(mario.paycheck)

mario.raise_paycheck(0.1)
print(mario.paycheck)

