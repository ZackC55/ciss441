"""
Author: Zack Cochran
Date: 04/12/2020
Goal: To take historical stock data on Microsoft (MSFT) and display it in a candlestick graph.
"""

# Import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.dates import date2num
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('msft.csv', parse_dates=True, index_col=0)

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(date2num)
print(df_ohlc.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(date2num), df_volume.values, 0)
plt.show()
