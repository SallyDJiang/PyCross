from createpicross import * 
from matplotlib.backend_bases import MouseButton

# ASKS USER WHICH MODE THEY WANT TO DO 
mode = input("Would you like to create or play a game? (Enter 'c' or 'p')")

# SET GLOBAL VARIABLE FOR IMAGE BEING USED BY ALL FUNCTIONS
image_array = ""

def set_mode(mode_status):
    '''
    allows user to set model of game, whether creating their own image or playing a preset image game
    
    Parameters
    ----------
    mode_status: str
        mode that user is playing in, either "C", create, or "P", play
        
    Returns
    -------
    bool: bool
        returns True if user is playing and False if user is just creating and messing around with image maker
    '''
    global image_array 
    if str(mode_status).strip().upper() == 'C': # player wants to create a game 

        # Setup
        filename = str(input("Path to desired image file (.png) \n"))
        size = int(input("Window Size?"))
        #make_game = str(input("Would you like to make a game with this image? (Y/N)"))

        image_array = load_image(img=filename, window_sizex=size, window_sizey=size)

        if isinstance(image_array, np.ndarray): 
            mode_status = 'p'
            return True
        else: 
            pass
    elif str(mode_status).strip().upper() == 'P': # player wants to play a game 
        image_array = load_image(img=None)
        return True
    
    else: 
        print("Please enter 'c' or 'p'")

def track_drawn(image, loc):
    '''
    tracks the locations that are drawn onto the board, and notes whether its a correctly
    colored square or correct. 
    
    Also tracks when all squares are colored in
    
    Parameters
    ----------
    image: str
        answer image, which is used to track the user's progress
        
    loc: array
        set of locations colored by user 
        
    '''
    global status
    xs, ys = np.where(image == 1)
    img_loc = [(y,x) for x,y in zip(xs,ys)]
    
    
    # runs when user finishes game, ie all colored squares match colored square in answers array
    if len(loc.intersection(img_loc)) == len(img_loc):
        
        print("FINISHED")
        plt.disconnect(click)
        plt.clf()
        plt.imshow(image, cmap="Greys", origin="lower")
        plt.axis("off")
        fig.canvas.draw()

def track_points(point, action, img):
    '''
    tracks the points the user has, and ends game if user gets too many wrongs
    
    Parameters
    ----------
    point: int
        current point count 
        
    action: str
        tells whether to add or subtract points 
        
    img: array
        uses image to determine when 25% of the squares are incorrectly colored, and where to add scoreboard (xy)
        
    Returns
        -------
    point: int
        updated points of user
    '''
    
    # insert the global variables to be used in function
    global fig
    global ax
    
    # check how to update points 
    if action == "add": 
        point += 1
    if action == "sub": 
        point -= 1
    
    # update scoreboard
    ax.texts[-1].set_visible(False)
    ax.text(x = np.shape(img)[0], y = np.shape(img)[1]/2, s="  Score: "+str(point), fontsize=15)
    
    # ends games if score too low
    if point <= -round((np.shape(img)[0] * np.shape(img)[1])/15): 
        plt.disconnect(click)
        ax.text(x=length/2, y=-1, s="Game OVER! TOO MANY WRONGS \n Score: "+str(point), fontsize=20, ha="center", color="blue")
        #ax.text(x = np.shape(img)[0]/2, y = np.shape(img)[1]/2, s="Game OVER! \n TOO MANY WRONGS \n Score: "+str(point), fontsize=50, ha="center", color="blue")
    fig.canvas.draw()
    return point
      
def on_click(event):
    '''
    main function that updates grid when user interacts with it, draws either square (left click)
    or X (right click) and checks if its right or wrong 
    
    Parameters
    ----------
    event: event
        checks what event the user is doing (Mouse click) 
      
    '''
    # insert the global variables to be used in function
    global loc 
    global x_loc
    global image_array
    global points 
    if event.inaxes:
        if event.button is MouseButton.LEFT: # coloring square
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
                
        if event.button is MouseButton.RIGHT: # allow user to mark X's where they want to keep track
            x = int(np.floor(event.xdata))
            y = int(np.floor(event.ydata))
            if (x, y) not in x_loc:
                ax.scatter(x+0.5, y+0.5, marker="x", s = (10*200/fig.dpi)**2, c="purple")
                x_loc.append((x, y))
            else: # allow user to remove X's if there was already one 
                ax.scatter(x+0.5, y+0.5, marker="s", s = (10*200/fig.dpi)**2, c="white")
                x_loc.remove((x, y)) 
            fig.canvas.draw()
     
    
# SETS STATUS DEPENDING ON WHETHER USER IS CREATING OR PLAYING A GAME
status = set_mode(mode)            

# SETUPS UP PLAYABLE GAME 
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

    


