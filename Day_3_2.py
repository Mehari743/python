
import pandas as pd 
import matplotlib.pyplot as plt 

# file= r'C:\Users\Assaye\Desktop\Python_Training\data\air.csv'
# df=pd.read_csv(
#     file,
#     sep=';',
#     na_values=[-200],parse_dates=[["Date","Time"]],usecols=["Date","Time","CO(GT)","T","RH","AH"]
#     ).rename(columns={"Date_Time":'tstamp','CO(GT)':'CO','T':'T','RH':'rel_hum','AH':'abs_hum'})
# print(df.head())

# #print(df.dtypes)

# # to extract only one column of paranmter
# #there must be a space b/n year and hour
# df["tstamp2"]=pd.to_datetime(df["tstamp"], format='%d/%m/%Y %H.%M.%S')
# #print(df.head())
# #print(df.dtypes)

# #to put the collun as an index

# df.index=df["tstamp2"]
# print(df.index)


# #print(df.index.min())

# #print(df.index.day_name())

# print(df.groupby(df.index.day_name())["CO"].mean().sort_values(ascending=False))

# #print(df.groupby(df.index.hour)["CO"].mean())

# # to agregate=day time value

# #print(df.groupby([df.index.day_name(),df.index.hour])["CO"].mean().sort_values(ascending=False))
# # to resample by month
# month_values=df.resample("M")["CO"].agg(["mean"])
# print(month_values)

# month_values=df.resample("M")["CO"].agg(["mean","max"])
# print(month_values)

# month_values=df.resample("W")["CO"].agg(["mean"])
# #print(month_values)

# month_values=df.resample("W")["CO"].agg(["mean","max"])
# #print(month_values)
# month_values.to_csv(r'C:\Users\Assaye\Desktop\Python_Training\data\month_mean.csv')


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


#gy=df.groupby("Year").sum()
#gy.plot(y="Deaths",kind='line')
#plt.show()

file1= r'C:\Users\Assaye\Desktop\Python_Training\data\d1.csv'
file2= r'C:\Users\Assaye\Desktop\Python_Training\data\d2.csv'

d1=pd.read_csv( file1)
d2=pd.read_csv(file2)

d3=d1.merge(d2,left_on="Code", right_on="Code",suffixes=('_left', '_right'))

print(d3.head())


































