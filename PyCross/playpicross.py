from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton
from createpicross import * 
import numpy as np
    

example_img = load_image(plot=False)

length , width = np.shape(example_img)
fig, ax = plot_hints(example_img, length, width)   

answer_array = example_img
loc = []

def track_drawn(image, loc):
    xs, ys = np.where(image == 1)
    img_loc = [(x,y) for x,y in zip(xs,ys)]
    if len(loc.intersection(img_loc)) == len(img_loc):
        print("FINISHED")
        plt.disconnect(click)
    

def on_click(event):
    global loc 
    if event.inaxes:
        if event.button is MouseButton.LEFT:
            x = int(np.floor(event.xdata))
            y = int(np.floor(event.ydata))
            if answer_array[y][x] == 1:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*100/fig.dpi)**2, c="black")
                fig.canvas.draw()
                loc.append((x, y))
                print(set(loc))
                track_drawn(answer_array, set(loc))
            else:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*100/fig.dpi)**2, c="red")
                fig.canvas.draw()
                
click = plt.connect('button_press_event', on_click)

plt.show()


def check_done(): 
    pass