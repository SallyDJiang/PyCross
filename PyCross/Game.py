from createpicross import * 
from matplotlib.backend_bases import MouseButton


mode = input("Would you like to create or play a game? (Enter 'c' or 'p')")

image_array = ""

def set_mode(mode_status):
    '''
    allows user to set model of game, whether creating their own image or playing a preset image game
    '''
    global image_array 
    if str(mode_status) == 'c': # player wants to create a game 

        # Setup
        filename = str(input("Please insert path to desired image file \nRecommended: .png, .jpeg \n"))
        size = int(input("How big would you like the window?"))
        make_game = str(input("Would you like to make a game with this image? (Y/N)"))

        image_array = load_image(img=filename, window_sizex=size, window_sizey=size)

        if isinstance(image_array, np.ndarray): 
            if make_game == "Y": 
                print("Making Game...")
                mode_status = 'p'
                return True
                
            elif make_game == "N": 
                print("Not Making Game")
                plt.imshow(image_array, cmap="Greys")
                plt.show()
                return False
               
            else: 
                print("Please enter Y or N into the terminal")
        else: 
            pass

    elif str(mode_status) == 'p': # player wants to play a game 
        image_array = load_image(img=None)
        return True
    
    else: 
        print("Please enter 'c' or 'p'")

# NOT WORKING, IGNORE
def track_drawn(image, loc):
    global status
    xs, ys = np.where(image == 1)
    img_loc = [(y,x) for x,y in zip(xs,ys)]
    if len(loc.intersection(img_loc)) == len(img_loc):
        print("FINISHED")
        plt.disconnect(click)
        fig, ax = plt.subplots()
        ax.imshow(image, cmap="Greys")
        fig.canvas.draw()

def on_click(event):
    global loc 
    global image_array
    if event.inaxes:
        if event.button is MouseButton.LEFT:
            x = int(np.floor(event.xdata))
            y = int(np.floor(event.ydata))
            if image_array[y][x] == 1:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*500/fig.dpi)**2, c="black")
                fig.canvas.draw()
                loc.append((x, y))
                print(set(loc))
                track_drawn(image_array, set(loc))
            else:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*500/fig.dpi)**2, c="red")
                fig.canvas.draw()
                
        if event.button is MouseButton.RIGHT:
            x = int(np.floor(event.xdata))
            y = int(np.floor(event.ydata))
            ax.scatter(x+0.5, y+0.5, marker="x", s = (10*200/fig.dpi)**2, c="purple")
            fig.canvas.draw()
            
            
status = set_mode(mode)            
if status is True: 
    print("PLAYING")
    length , width = np.shape(image_array)
    fig, ax = plot_hints(image_array, length, width) 
    ax.text(length/6, -1, "Left click to color in square, Right click to mark Board", fontsize=20)
    loc = []
    click = plt.connect('button_press_event', on_click)
    plt.show()

elif status is False:
    print("CREATING")

def points():
    pass

    


