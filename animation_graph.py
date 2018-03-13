import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')
ax1 = plt.subplot2grid((1,1),(0,0))


def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    yx = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)

# 这是动态图片的最基本语句，这样每当我们数据集变化的时候，就可以直接在图像上面显示出来而不需要重新运行（实际上是
# python在后台代替我们重新运行），interval代表python自动更新图像的时间，1000ms。
ani = animation.Funcanimation(fig, animate, interval=1000)
