import quandl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### Data Management ###
# retrieve data from quandl api
# aapl = quandl.get("WIKI/AAPL", start_date="2006-10-01", end_date="2012-01-01")

# export to csv
# aapl.to_csv('../data/aapl_ohlc.csv')

# load pandas df from csv
aapl = pd.read_csv('../data/aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)


### Data Manipulation ###
# add a column `Daily Difference` to `aapl`
aapl['Daily Difference'] = aapl['Adj. Open'] - aapl['Adj. Close']

# calculate the percentage change
aapl['Percentage Change'] = aapl['Daily Difference'] / aapl['Adj. Close']

# calculate the log percentage daily change
aapl['Log Percentage Change'] = np.log(aapl['Percentage Change']+1)

# resample `aapl` to quarters, take the mean as value per quarter
quarter = aapl.resample("4M").mean()

# print(quarter.tail())

# delete the new `diff` column
# del aapl['diff']


### Analysis ###
# print first few lines of df for rows associated with year 2007
# print(aapl.loc['2007'].head())

# plot the closing prices for `aapl`
# aapl['Close'].plot(grid=True)

# Plot the distribution of `daily_pct_c`
aapl['Log Percentage Change'].hist(bins=50)

# show the plot
# plt.show()
