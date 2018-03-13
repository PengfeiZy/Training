import pandas as pd
import datetime as dt
import pandas_datareader.data as web
from matplotlib import style
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use('ggplot')
ax1 = plt.subplot2grid((6,1),(0,0), rowspan=3, colspan=1)
ax2 = plt.subplot2grid((6,1),(4,0), rowspan=2, colspan=1, sharex=ax1)

def get_stock_data(ticker):

    start = dt.datetime(2005,1,1)
    end = dt.datetime.today()

    df = web.DataReader(ticker, 'yahoo', start, end)

    return df

df = get_stock_data('tsla')

df_ohlc = df['Adj Close'].resample('10d').ohlc()
df_volume = df['Volume'].resample('10d').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
candlestick_ohlc(ax1, df_ohlc.values, width=5, colorup='g')
ax1.xaxis_date()

ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0, alpha=0.3)

plt.show()

