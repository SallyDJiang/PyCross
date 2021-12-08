from createpicross import * 
from matplotlib.backend_bases import MouseButton


mode = input("Would you like to create or play a game? (Enter 'c' or 'p')")

image_array = ""

def set_mode(mode_status):
    '''
    allows user to set model of game, whether creating their own image or playing a preset image game
    '''
    global image_array 
    if str(mode_status).strip().upper() == 'C': # player wants to create a game 

        # Setup
        filename = str(input("Please insert path to desired image file \nRecommended: .png, .jpeg \n"))
        size = int(input("How big would you like the window?"))
        make_game = str(input("Would you like to make a game with this image? (Y/N)"))

        image_array = load_image(img=filename, window_sizex=size, window_sizey=size)

        if isinstance(image_array, np.ndarray): 
            if make_game.strip().upper() == "Y": 
                print("Making Game...")
                mode_status = 'p'
                return True
                
            elif make_game.strip().upper() == "N": 
                print("Not Making Game")
                plt.imshow(image_array, cmap="Greys")
                plt.show()
                return False
               
            else: 
                print("Please enter Y or N into the terminal")
        else: 
            pass

    elif str(mode_status).strip().upper() == 'P': # player wants to play a game 
        image_array = load_image(img=None)
        return True
    
    else: 
        print("Please enter 'c' or 'p'")

        

def track_drawn(image, loc):
    global status
    xs, ys = np.where(image == 1)
    img_loc = [(y,x) for x,y in zip(xs,ys)]
    if len(loc.intersection(img_loc)) == len(img_loc):
        print("FINISHED")
        plt.disconnect(click)
        plt.clf()
        plt.imshow(image, cmap="Greys", origin="lower")
        plt.axis("off")
        fig.canvas.draw()

def track_points(point, action, img):
    global fig
    global ax
    if action == "add": 
        point += 1
    if action == "sub": 
        point -= 1
     
    ax.texts[-1].set_visible(False)
    ax.text(x = np.shape(img)[0], y = np.shape(img)[1]/2, s="Score: "+str(point), fontsize=15)
    if point <= -round((np.shape(img)[0] * np.shape(img)[1])/4): 
        plt.disconnect(click)
        ax.text(x = np.shape(img)[0]/2, y = np.shape(img)[1]/2, s="Game OVER! TOO MANY WRONGS \n Score: "+str(point), fontsize=15)
    
    fig.canvas.draw()
    return point
      
def on_click(event):
    global loc 
    global x_loc
    global image_array
    global points 
    if event.inaxes:
        if event.button is MouseButton.LEFT:
            x = int(np.floor(event.xdata))
            y = int(np.floor(event.ydata))
            if image_array[y][x] == 1:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*500/fig.dpi)**2, c="black")
                fig.canvas.draw()
                loc.append((x, y))
                track_drawn(image_array, set(loc))
                points = track_points(points, "add", image_array)
            else:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*500/fig.dpi)**2, c="red")
                points = track_points(points, "sub", image_array)
                fig.canvas.draw()
                
        if event.button is MouseButton.RIGHT:
            x = int(np.floor(event.xdata))
            y = int(np.floor(event.ydata))
            if (x, y) not in x_loc:
                ax.scatter(x+0.5, y+0.5, marker="x", s = (10*200/fig.dpi)**2, c="purple")
                x_loc.append((x, y))
            else:
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*200/fig.dpi)**2, c="white")
                x_loc.remove((x, y)) 
            fig.canvas.draw()
            
            
status = set_mode(mode)            
if status is True: 
    print("PLAYING")
    length , width = np.shape(image_array)
    fig, ax = plot_hints(image_array, length, width) 
    ax.text(length/6, -2, "Left click to color in square, Right click to mark Board", fontsize=20)
    points = 0
    loc = []
    x_loc = []
    click = plt.connect('button_press_event', on_click)
    plt.show()

elif status is False:
    print("CREATING")

    


