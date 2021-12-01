# https://matplotlib.org/3.4.3/users/event_handling.html

from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

class Scatter_Draw: 
    def __init__(self, point):
        self.point = point 
        self.xs = list(point.get_xdata())
        self.ys = list(point.get_ydata())
        self.cid = point.figure.canvas.mpl_connect('button_press_event', self)
    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.point.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.point.set_data(self.xs, self.ys)
        self.point.figure.canvas.draw()
            
fig, ax = plt.subplots()
ax.set_title('Picross Player')
point, = ax.plot([], [], linestyle="none", marker="s", color="r", markersize=10)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.grid(which='major', color='#CCCCCC', linestyle='-')
ax.set_xticklabels("")
ax.set_yticklabels("")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
linebuilder = Scatter_Draw(point)


plt.show()

# Save points 

# Take saved points and check if they are within the answers 

def color_square(example_array, x, y):
    
    if example_array[y][x] == 1:
        axes.plot(x+0.5,y-0.5, marker="s", ms = (10*65/figure.dpi)**2, c="black")
        array[y][x] = 1
        return figure, True
    else: 
        array[y][x] = 0
        axes.plot(x+0.5,y-0.5, marker="s", ms = (10*65/figure.dpi)**2, c="red")
        print("Wrong Tile")
        return figure, False
    
#plt.imshow(array, origin="lower")