from matplotlib import pyplot as plt
import numpy as np 


fig, ax = plt.subplots()
ax.set_title('click on points')

line, = ax.plot(np.random.rand(100), 'o',
                picker=True, pickradius=5)  # 5 points tolerance

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    if (thisline.get_xdata() > 0) & (thisline.get_xdata() < 50):
        print("Invalid")
    
    print('onpick points:', points)

fig.canvas.mpl_connect('pick_event', onpick)


plt.show()