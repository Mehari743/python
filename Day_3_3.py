import pandas as pd 
import matplotlib.pyplot as plt 
#plotting function

file=r'C:\Users\Assaye\Desktop\Python_Training\data\natural_disasters.csv'

df=pd.read_csv(file)

df.plot()

#df.plot(x='Year',y='Deathes')

#df.groupby("Entity").mean()

gb=df.groupby("Entity").mean()

gb.plot(y="Deaths", kind='bar',color='red')
#groupby year with mean aggregation function and make the plot of type line where Y axis=Deaths

# gy=df.groupby("Year").mean()
# gy.plot(y="Deaths",kind='line')
# plt.show()


gy=df.groupby("Year").sum()
gy.plot(y="Deaths",kind='line')
plt.show()

file1= r'C:\Users\Assaye\Desktop\Python_Training\data\d1.csv'
file2= r'C:\Users\Assaye\Desktop\Python_Training\data\d2.csv'

d1=pd.read_csv( file1)
d2=pd.read_csv(file2)

d3=d1.merge(d2,left_on="Code", right_on="Code",suffixes=('_left', '_right'))

print(d3.head())




















