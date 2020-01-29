import pandas as pd

d=[10,30,40]
i=[1,2,3]
s=pd.Series(d,i)
print(s)

d={'a':10,'b':20,'c':30}
sd=pd.Series(d)
#print(sd)
#print(sd.index)
#index
print(sd[2])

l=[10,3,6,7,8]
df=pd.DataFrame(l)
print(df)
# dictionary
d={'one':[1,2,3],'two':[4,5,6],'three':[7,8,9]}
df=pd.DataFrame(d)
print(df)
print(df['one'])
df["four"]=df["one"]+df["two"]
print(df)

del df["four"]

df["five"]=9

print(df["one"][1])


df.index=[1,2,3]
print(df)
print(df.iloc[0])

print(df.iloc[1])

#df.rename(colums={'one':'ONE'}, inplace=True)
#print(df)

file=r'C:\Users\Assaye\Desktop\Python_Training\data\natural_disasters.csv'
natural=pd.read_csv(file)
print(natural)


#print(natural.head())

#print(natural["Entity"]=='Fllod')
#sub=natural[natural["Entity"]=='Flood']
#print(sub)
#sub=natural[(natural["Entity"]=='Flood') & (natural["Year"]>1950)]
#print(sub)

#sub=natural[(natural["Entity"]=='Flood') | (natural["Year"]>1950)]
#print(sub)

sub=natural[(natural["Entity"]=='Flood') | (natural["Entity"]== 'Earthquake')]
print(sub)

#print(natural.describe())
#print(natural["Deaths"].describe())
#print(natural[["Year","Deaths"]].describe()).round(2))
#print(natural["Deaths"].sum())
print(natural.head())
natural["Deaths"].idxmax()
print(natural.iloc[natural["Deaths"].idxmax()])

gp=natural.groupby("Entity")["Deaths"].mean()
print(gp)

gp=natural.groupby("Entity")["Deaths"].sum()
print(gp)
e=natural[natural["Entity"]=='Earthquake']
print(e["Deaths"].sum())
#or
t=natural[natural["Entity"]=='Earthquake'].groupby("Entity")["Deaths"].sum()
print(t)

#m=natural[[(natural["Entity"]=='Earthquake' & (natural["Entity"])=='Flood')]. groupby("Entity")["Deaths"][Year]<=1950-1980].sum()
#print(m)

f=natural[(natural["Entity"]=='Flood') & (natural["Year"]>=1950) & (natural["Year"]<=1980)]
print(f["Deaths"].mean())



