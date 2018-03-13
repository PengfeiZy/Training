import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc

import numpy as np
import urllib
import datetime as dt
    

def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    
    # Unfortunately, Yahoo's API is no longer available
    # feel free to adapt the code to another source, or use this drop-in replacement.
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'Volume' not in line:
                stock_data.append(line)

# 注意np.loadtxt需要把所有格式都转化成float的格式，对于bytes的日期时间我们需要用到mdates
# 中间的bytepdate2num
    date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: mdates.bytespdate2num('%Y-%m-%d')})

    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x+=1

    # 注意蜡烛图的参数传入的原则，是list，且每一个元素是一个tuple，tuple俩面的值全部为float
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    



    #################################################新增内容，如何在图上相应位置加上文字和箭头, 注意我们这里的
    # 数据保存格式都是越靠近当前时间，其在列表的位置越靠前
    font_dict = {'family':'arial', 'color':'#ff0000', 'size':15}
    ax1.text(date[-10], closep[-10], 'This is a text', fontdict=font_dict)

    ax1.annotate('Bad News', (date[300], lowp[300]), xytext=(0.8, 0.9), textcoords='axes fraction',
                arrowprops=dict(facecolor='grey', color='red'))

    ### 把最靠近右边（即当前价格）标注在图上

    bbox_props = dict(boxstyle='larrow', fc='w', ec='k', lw=1)
    ax1.annotate(str(closep[0]), (date[0], closep[0]), xytext=(date[0]+20, closep[0]),
                bbox=bbox_props)


    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.90, top=0.90, wspace=0.2, hspace=0)
    plt.show()
    return closep

closep = graph_data('EBAY')
