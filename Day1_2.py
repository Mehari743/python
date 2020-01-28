s='john'
#print(dir(s))
s=s.upper()
print(s)
#print(help(s.q))
l=[1,2,3,4,5]
print(dir(l))
print(help(l.append))
print(help(s.upper))

# append
l.append(100)
print(l)

# insert
help(l.insert)
l.insert(0,100)
print(l)

# pop
help(l.pop)
print(l.pop)

# sort
l=[2,1,4,79,3,100,50]
l.sort()
print(l)

# reverse
l.sort(reverse=True)
print(l)

# dictionaries fucnction
d= {'Italy':'Rome','Germany': 'Berlin','Spain': 'Madrid'}
print(dir(d))
print(help(d.keys))
print(d.keys())
print(d.values())
print(d.items())

# loops ( for and while loops)

l=[1,2,3,4,5,6,7,8,9,10]
#for i in l:
   # print(i)

l=[1,2,3,4,5,6,7,8,9,10]
#for i in l:
    #print(i+10)

l=[1,2,3,4,5,6,7,8,9,10]
#for i in l:
    #print(i+10)
    #print(i)

l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i+10)
    print(i)
    print(i)


l1=[10,20,30,40]
l2=('A','B','C','D')
lt=[l1,l2]

for i in lt:
        print(i)

# loops in loops

l1=[10,20,30,40]
l2=('A','B','C','D')
lt=[l1,l2]
#for i in lt:
        #for j in i:
           # print(j)
           
#for i in lt:
        #for j in i:
           #print(j)
           #print(i)

for i in lt:
        for j in i:
           print(j)
           print(i)
           print(i)
           print(j)

# enumerate
for i,j in enumerate(l1):
        print(i,j)

#while loop
val=0
while val<20:
        print(val)
        #val=val+2
        val +=2

# exrecies
d={'name':['Johen','Maria','Anan'],'age':[21,25,13]} 
for k in d.keys():
        print(k)
for v in d.values():
        print(v)
for i in d.items():
        print(i)
for k,v in d.items():
        print(k,v)

# if,elif,else
l1=[10,20,30,40,50,60]
#if len(l1)>5:
       # print('I am along list')

#exrecise
d={'names':['Johen','Maria','Anan'],'age':[21,25,13]} 
for k,v in d.items():
        if k=='names':
            print(v)
else:
        print('I do not know what to do')
          

