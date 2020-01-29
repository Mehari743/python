# range
# r=range(1,100)
# print(r)

# l=list(r)
# print(l)

#d={'a':[1,2,3,...,50],'b':[1,2,3,...,20]}
# questions
# if the key is 'a' print values>25 if not print(no values)
# if the key is 'b' print values< 10 if not  don do anything
# sloution,first we have to creat the range
# ra=list(range(1,50))
# rb=list(range(1,20))
# d={'a':ra,'b':rb}
#d={'a':list(range(1,50)),'b':list(range(1,20))}
# print(d)

#for k,v in d.items():
#     if k=='a':
#         for i in v:
#             if i>25:
#               print(i)
#             else:
#                print('no valuse')


    #    if k=='b':
    #       for i in v:
    #         if i<10:
    #             print(i)
    #         else:
    #             print('don do anything')


#  print(d['a'])

#  l={}

#  for i in d['a']:
#     if i>25:
#         l.append(i)
#         print(l)


# Function
    #  def my_function():
    #    print('Hi,python')
    #  '''
    #   this function prints something
    #   this function does not need parameters
    #   print('Hi python')
    #   '''
    #  my_function()


    # def my_function2(s):
    #      print(s)

    # my_function2('Assaye')

#other example
    # def my_function3(name,age=33):
    #   print(name,age)
    # my_function3('Assaye')
    # def my_function3(name='Matteo',age=33):
    #     print(name,age)
    # my_function3(44,'Joe')

# multiplication
# def multiply(x,y):
#     result=x*y
#     print(result)
# multiply(10,35)

#list/argumnets
l=[10,2,3,50]

# def multiply2(*args):
#     v=1
#     for i in args:
#       v=v*i
#     print(v)
# multiply2(*l)

# def multiply2(*args):
#     v=1
#     for i in args:
#        v=v*i
#     return v
# mynumber=multiply2(*l)
# print(mynumber)

#To calculate the area
# def rect_area(width,height):
#     calculation=width*height
#     return calculation
# my_area=rect_area(100,40)
# print(my_area)

# def shape_area(shape,width,height):
#     if shape=='rectangle':
#       calculation=width*height 
#     if shape=='triangle':
#       calculation=width*height/2
#     else:
#        print(' I do not know the shape')
#     return calculation
# area=shape_area('triangle',100,5)
# print(area)

# unit conversion
# def fahrenhaite(celcius):
#     f=(celcius*9/5)+32
#     return f
# a=fahrenhaite(100)
# print(a)

# lc=[100,0,100,50]
# def fahrenheit2(*args):
#     lf=[]
#     for c in args:
#         calculation=(c*9/5)+32
#         lf.append(calculation)
#     return lf
# my_f=fahrenheit2(10,0,100,33)
# print(my_f)
# my_f2=fahrenheit2(*lc)
# print(my_f2)

# lc=[100,0,100,50]
# def fahrenheit2(*args):
#      lf=[]
#      for c in args:
#         calculation=(c*9/5)+32
#         lf.append(calculation)
#      return lf
# my_f=fahrenheit2(10,0,100,33)
# print(my_f)
# my_f2=fahrenheit2(*lc)
# print(my_f2)



