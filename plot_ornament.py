import pandas as pd
import urllib.request
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

ax1 = plt.subplot2grid((1,1),(0,0))

data = urllib.request.urlopen('https://pythonprogramming.net/yahoo_finance_replacement').read().decode()
with open('example.csv','w') as f:
    f.write(data)

df = pd.read_csv('example.csv')

date, closep = df['Date'], df['Close']

time = []
for row in date:
    time.append(dt.datetime.strptime(row, '%Y-%m-%d'))

closep = np.array(closep.tolist())
time = np.array(time)

ax1.plot_date(time, closep, '-', label='Stock Price')

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

ax1.plot([],[],linewidth=5, label='loss', color='r',alpha=0.5)
ax1.plot([],[],linewidth=5, label='gain', color='g',alpha=0.5)

ax1.fill_between(time, closep, closep[0], where=(closep < closep[0]), facecolor='r', alpha=0.5)
ax1.fill_between(time, closep, closep[0], where=(closep > closep[0]), facecolor='g', alpha=0.5)

ax1.grid(True)#, color='g', linestyle='-', linewidth=5)
ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')
ax1.set_yticks([0,25,50,75])
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('stock')
plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    

plt.show()
