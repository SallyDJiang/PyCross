from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton

from createpicross import * 
import numpy as np
    

example_img = load_image(plot=False)

length , width = np.shape(example_img)
fig, ax = plot_grid(length, width)   

answer_array = example_img

def on_click(event):
    if event.inaxes:
        if event.button is MouseButton.LEFT:
            x = int(np.floor(event.xdata))
            y = int(np.floor(event.ydata))
            print(x,y)
            if answer_array[y][x] == 1:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*100/fig.dpi)**2, c="black")
                fig.canvas.draw()
            else:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*100/fig.dpi)**2, c="red")
                fig.canvas.draw()
                

plt.connect('button_press_event', on_click)

plt.show()
