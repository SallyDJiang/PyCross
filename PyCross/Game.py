from createpicross import * 
#from playpicross import * 

mode = input("Would you like to create or play a game? (Enter 'c' or 'p')")


def set_mode(mode_status):

    if str(mode_status) == 'c': # player wants to create a game 
        
        # Setup
        filename = str(input("Please insert path to desired image file \nRecommended: .png, .jpeg \n"))
        size = int(input("How big would you like the window?"))
        make_game = str(input("Would you like to make a game with this image? (Y/N)"))
        
        image_array = load_image(img=filename, window_sizex=size, window_sizey=size)

        if isinstance(image_array, np.ndarray): 
            if make_game == "Y": 
                print("Making Game...")
                # run playpicross main (game) 
                length, width = np.shape(image_array)
                plot_hints(image_array, length, width)
                plt.show()

            elif make_game == "N": 
                print("Not Making Game, plotting image")
                # run playpicross main (answer sheet)
                image_array = load_image(img=filename, window_sizex=size, window_sizey=size)
                plt.imshow(image_array, cmap="Greys")
                plt.show()
            else: 
                print("Please enter Y or N into the terminal")
        else: 
            pass
            
    elif str(mode_status) == 'p': # player wants to play a game 
        # run playpicross 
        pass

    else: 
        print("Please enter 'c' or 'p'")
            

set_mode(mode)


def points():
    pass

    
    


