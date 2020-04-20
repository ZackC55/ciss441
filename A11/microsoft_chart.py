"""
Author: Zack Cochran
Date: 04/12/2020
Goal: To take historical stock data on Microsoft (MSFT) and display it for a specified time period.
"""

import datetime as dt
import matplotlib.pyplot as pyplot
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('MSFT', 'yahoo', start, end)
print(df.tail(6))

df.to_csv('msft.csv')
