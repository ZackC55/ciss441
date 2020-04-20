"""
Author: Zack Cochran
Date: 04/12/2020
Goal: To take historical stock data on Microsoft (MSFT) and display it in a graph format.
"""

# Import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('msft.csv', parse_dates=True, index_col=0)
print(df[['Open', 'High']].head())
df['Adj Close'].plot()
plt.show()
