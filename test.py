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
    df = df / df.iloc[0]
    return df

def time_of_operation(func, *args):
    t0 = time()
    result = func(*args)
    t1 = time()
    return result, t1 - t0

start_date = '2008-01-01'
end_date = '2018-11-18'
# symbols = ['FB', 'SQ', 'TWTR', 'SNAP', 'AMZN', 'MSFT', 'NFLX', 'AAPL']
symbols = ['FB', 'SQ']
df = get_data(symbols)
# # plot_data(df, 'Since Snapchat IPO', 'Relative Performance')
# print(np.ndarray(df.values))

print(df.std())
