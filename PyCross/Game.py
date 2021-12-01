from createpicross import * 
#from playpicross import * 


mode = input("Would you like to create or play a game? (Enter 'c' or 'p')")

def set_mode(mode_status):
    if str(mode_status) == 'c': # player wants to create a game 
        
        # Setup
        filename = str(input("Please insert path to desired image file \nRecommended: .png, .jpeg \n"))
        size = int(input("How big would you like the window?"))
        make_game = str(input("Would you like to make a game with this image? (Y/N)"))
        
        
        if make_game == "Y": 
            image_array = load_image(img=filename, plot=False, window_sizex=size, window_sizey=size)

            print("Making Game...")
            length, width = np.shape(image_array)
            plot_hints(image_array, length, width)
            plt.show()

        elif make_game == "N": 
            print("Not Making Game, plotting image")
            image_array = load_image(img=filename, plot=True, window_sizex=size, window_sizey=size)
            plt.show()
        else: 
            print("Please enter Y or N")
            
    elif str(mode_status) == 'p': # player wants to play a game 
        pass

    else: 
        print("Please enter 'c' or 'p'")
            
            
set_mode(mode)

    


