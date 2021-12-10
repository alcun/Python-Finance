import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr


yf.pdr_override()

stock = input("Enter a stock ticker symbol: ")
print(stock)

startyear = 2019
startmonth = 1
startday = 1 

start = dt.datetime(startyear,startmonth,startday)

now = dt.datetime.now()

df = pdr.get_data_yahoo(stock,start,now)

print(df)

'''
sets range of SMA window
'''

ma = 50

'''
lets sma work as string
'''
smaString = "Sma_" + str(ma)

df[smaString]=df.iloc[:,4].rolling(window = ma).mean()

print(df)

'''
cuts out first ma values
'''

df = df.iloc[ma:]



'''
check if closing value is above or below moving average
remove prior print(df here to just see dates)
'''

for i in df.index:
	print(i)



'''compare ith value of ma and adj close'''




numH = 0
numC = 0

for i in df.index:
	if(df["Adj Close"][i] > df[smaString][i]):
		print("The Close is Higher")
		numH+=1
	else:
		print("The Close is Lower")
		numC+=1

print("The Close Was Higher", (str(numH), "times"))
print("The Close Was Lower", (str(numC), "times"))


'''for i in df.index:
	if(df["Adj Close"][i] > df[smaString][i]):
		print("The Close is Higher")
	else:
		print("The Close is Lower")'''



'''for i in df.index:
	print(df["Adj Close"][i])'''

'''for ma values replace ^ withfor i in df.index:
	print(df.iloc[:,4][i]) '''

'''for ma values replace ^ with 
for i in df.index:
	print(df[smaString][i])'''