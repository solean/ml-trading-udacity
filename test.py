import os
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr
import fix_yahoo_finance as yf
import numpy as np
import time
# for debugging only
import pdb

yf.pdr_override()


def plot_data(df, title, y_label):
    chart = df.plot(title=title)
    chart.set_ylabel(y_label)
    plt.show()

def get_data(symbols):
    data = pdr.get_data_yahoo(symbols, start=start_date, end=end_date)
    df = data['Adj Close']

    # slicing rows and columns at the same time
    # df = df.ix['2018-10-01':'2018-11-16', ['SLV', 'GLD']]

    df = df.dropna()
    # df.fillna(method='bfill', inplace='TRUE')
    # df.fillna(method='ffill', inplace='TRUE')
    df = df / df.iloc[0]
    return df

def time_of_operation(func, *args):
    t0 = time()
    result = func(*args)
    t1 = time()
    return result, t1 - t0

def get_daily_returns(df):
    daily_returns = (df / df.shift(1)) - 1
    # set daily returns for row 0 to 0
    daily_returns.iloc[0, :] = 0
    return daily_returns

def plot_histogram(df):
    df.plot()
    df.hist(bins=20)
    # mean = df.mean()
    # std = df.std()
    # plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)

def plot_scatter(df, x, y):
    df.plot(kind='scatter', x=x, y=y)
    beta_SQ, alpha_SQ = np.polyfit(df[x], df[y], 1)
    plt.plot(df['SPY'], beta_SQ*df[x] + alpha_SQ, '-', color='r')



start_date = '2008-01-01'
end_date = '2018-11-18'
# symbols = ['FB', 'SQ', 'TWTR', 'SNAP', 'AMZN', 'MSFT', 'NFLX', 'AAPL']
symbols = ['FB', 'SQ', 'SPY']
df = get_data(symbols)
df = get_daily_returns(df)
plot_scatter(df, x='SPY', y='SQ')
plt.show()

# print(df.kurtosis())
# print(df.corr(method='pearson'))
