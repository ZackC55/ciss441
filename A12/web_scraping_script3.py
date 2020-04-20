"""
Author: Zack Cochran
Date: 04/19/2020
Goal: To web scrap a website with data on the coronavirus by state and then create a visualization of that data.
"""

from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import matplotlib.pyplot as plt

### Reference
### https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
### https://datatofish.com/sort-pandas-dataframe/
### https://kite.com/python/answers/how-to-rotate-axis-labels-in-matplotlib-in-python

### Downloading the Website data's collapse1 tag
URL = 'https://www.city-data.com/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results_collapse1 = soup.find(id= 'collapse1')

### Scrape & Save
state_elems = results_collapse1.find_all('tr')
state_data = []
for s_ct, state_row in enumerate(state_elems):
    columns_col = state_row.find_all('td')
    if columns_col:
        state_tag, confirmed_tag, recovered_tag, active_tag, deaths_tag = columns_col
        state_data.append([
            str(state_tag.text),
            int(confirmed_tag.text.replace(',','')),
            int(deaths_tag.text.replace(',',''))
        ])
df = pd.DataFrame(state_data, columns = ['State', 'Confirmed', 'Deaths'])
df.to_csv(os.path.join('data', 'city_covid_data.csv'))

### Visualization
df.sort_values(by=['Confirmed'], inplace=True, ascending=False)
print(df.head(10))
ax = df.head(10).plot.bar(x='State', y=('Confirmed','Deaths'), rot=0)
plt.xticks(rotation=45)
plt.show()
