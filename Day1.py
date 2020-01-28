# this my comment
i=10
print(i)

s='Assaye'
print(s)
s="Bob's Cat and Alice's dog"
print(s)
#s='My name is Assaye'
#print(s)
# to write in coloumn
s='My name is\n Assaye'
print(s)
# booleans
mybool1=True
mybool2=False
print(mybool1, mybool2)
#strings
i=1
print(str(i))

s='1'
conv=int(s)

#Lists and dictionary
l=[1,2,3,4,5]
print(type(l))
x=[1,2,True]
print(type(x))

m=[1,2,3,1,1,1,1]
print(m)
#set
s1=set(m)
print(s1)
print(type(s1))

# to know the first number
y=[1,2,3,4,1,1,1,1,2,2,3,3,3,3,3,3]
print(y[0])
# to know the last number
print(y[-1])

# to know the first lists
print(y[0:3])

k=[1,2,3,4,5,6,7,8,9,10]
print(k[0:3])

print(k[0:4])
# to know the upto the last 2 remaining numbers
print(k[:-2])

# concanticate
l1=[1,2,3]
l2=[4,5,6]
lm=(l1,l2)
print(lm)

# to know the type
t=[1,2,3]
print(type(t))
#tuple
r=(1,2,4,5)
print(type(r))

# dictionaries
d={'name':'Matteo','age':33}
print(d)
print(d['name'])
d['name']='Matteo'
d={'name':['jeo','Matteo','Johen']}
print(d['name'][-1])
# wriet you name, surname, and your age
#information= f''' my compelte name is {'name'} {'surname'} and 'I am' {age} old '''
information= f''' my compelte name is {'Assaye Mehari'} {'Kidanemariam'} and 'I am' {31} old '''
print( information)

# three ways to write the names
name='Assaye'
complete_name= 'My name is %s' % name
print(complete_name)
#2nd option
complete_name='My name is{}'.format(name) 
print(complete_name)

#3rd option
complete_name=f'My name is {name}'
print(complete_name)


# to know the length
l=(1,2,3,4,1,1,1,1,1,2,2,3,3,3,3,3)
print(l)
print(len(l))


# dictionaries
d={'name':['jeo', 'Matteo','johen'],'number':30,'string': 'I am a string'}
print(d)

