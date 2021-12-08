# Load Package Dependents 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import random
from PIL import Image

# Set Style 
style = 'default'
plt.style.use(style)
plt.rcParams['font.family'] = 'fantasy'
 
# takes image given by user and rebinned the image 
def img2bw(im, threshold = 50):
    '''
    Takes in an image and takes features from it into another array with 0 for no
    notable features and 1 as having notable features. 
    
    Turns array of color into binary, black and white image 
    
    Parameters
    ----------
    im: array_like
        original 2D array of image 
    threshold: int
        picks the threshold at which to select features in image 
    Returns
    -------
    rebinned: array_like
        rebinned and binary array with the important features of original image
    '''
    
    length, width = np.array(im).shape[:2]
    
    rebinned = np.zeros((length,width))
    for x in np.arange(0, length):
        for y in np.arange(0, width):
            if im[x:x+1, y:y+1].mean() > threshold:
                rebinned[x:x+1, y:y+1] = 1
    return rebinned

# loads in the image and shows the user what the image is 
# if no image is provided then a preset image is set and shown 

def load_image(img=None, window_sizex=20, window_sizey=20):
    '''
    loads the image that is to be the basis of the picross puzzle

    Parameters
    ----------
    img: array_like
        image to be used  
    window_sizex: int
        size of x component of image (Default: 20) 
    window_sizey: int
        size of y component of image (Default: 20) 
    Returns
    -------
    rebinned: array_like
        rebinned and binary array with the important features of original image
    '''
    
    corr_window_sizex, corr_window_sizey = check_window_size(window_sizex, window_sizey)
    
    try: 
        if check_image_loaded(img)[0] == True:
            print("Image Provided, Returning Image....")
            image_array = check_image_loaded(img)[1]
            resized_image = np.array(image_array.resize((corr_window_sizex, corr_window_sizey))) 
            image_array = np.array(img2bw(resized_image))
            return image_array
            
        elif check_image_loaded(img)[0] == False: 
            print("No Image Provided, Returning Preset Image....")
            image_array = check_image_loaded(img)[1] 
            return image_array
        else: 
            pass
    except TypeError:
        pass


def check_window_size(win_sizex, win_sizey):
    '''
    checks window size choosen by user and makes sure it is less than 40x40 pixels 

    Parameters
    ----------
    win_sizex: int
        size of window (x component)
    win_sizey: int
        size of window (y component)
    Returns
    -------
    win_sizex, win_sizey: tuple (int)
        returns back the window sizes (x and y) if not too big, 
        or returns max size, if too big
    '''
    if win_sizex > 40: 
        win_sizex = 40
        print("X-window size too large, using size", win_sizex, "instead")
    if win_sizey > 40: 
        win_sizey = 40
        print("Y-window size too large, using size", win_sizey, "instead")        
    return win_sizex, win_sizey
    
    
def check_image_loaded(image=None): 
    '''
    checks that the image needed to load is loaded properly, if no 
    image is given, it returns back a random preset image 
    
    Parameters
    ----------
    image: str
        path to image (default = None) 
    Returns
    -------
    bool, img : bool, array
        returns back image and a boolean, True if the user had given an image and
        it was loaded in properly, False if no image provided and preset image was used
    '''

    if image is None: 
        image_array = set_preset_image()
        return False, image_array
    else:
        try: 
            loaded_image = Image.open(image)
            img = check_image_size(loaded_image)
            return True, img
        
        except FileNotFoundError: 
            print("Image not Valid, Please enter valid format for image (.png, .jpeg, .jpg) or Check the filepath. ")
            pass
        
def check_image_size(image): 
    '''
    checks the size of the image, the user is trying to use, if it is too big, let the user know 
    
    Parameters
    ----------
    image: array
        image array
    Returns
    -------
    image: array
        returns back image if not too big, if image too big, does not return back anything
    '''
    if (np.array(image).shape[0] >= 500) and (np.array(image).shape[1] >= 500):
        print("Image is too Big! Please restrict image to 500x500 pixels")
        pass
    
    elif (np.array(image).shape[0] <= 3) and (np.array(image).shape[1] <= 3):
        print("Image is too Small! Please add an image greater than 3x3 pixels")
        pass
        
    else:
        return image
    
    
    
def set_preset_image(): 
    '''
    selects a random image from a preset array dictionary
    
    Returns
    -------
    image: array
        returns back a random image from the already preset images 
    
    '''

    images = {"GALAXY": np.array(img2bw(np.array(Image.open("images/galaxy.png").resize((15, 15))))),
              "STAR": np.array(img2bw(np.array(Image.open("images/star.png").resize((15, 15))))),
              "ROCKET":  np.array(img2bw(np.array(Image.open("images/rocket.png").resize((10, 10))))),
              "COMET":np.array(img2bw(np.array(Image.open("images/comet.png").resize((10, 10))))),
              "BLACKHOLE":np.array(img2bw(np.array(Image.open("images/comet.png").resize((15, 15))))),
              "SOLARSYSTEM":np.array(img2bw(np.array(Image.open("images/solarsystem.png").resize((15, 15))))),
              "ATOM":np.array(img2bw(np.array(Image.open("images/atom.png").resize((20, 20)))))
                }
    
    return random.choice(list(images.values()))


def plot_grid(length, width): 
    '''
    plot the grid with the coordinates of each box depending on the size, specifed by the function
    
    Parameters
    ----------
    length: int
        length of image to plot
    width: int
        width of image to plot
        
    Returns
    -------
    fig, ax: figure and subplot
        returns back an image with the size given by the length and width, with equal spaced grid
    '''
    fig, ax = plt.subplots(figsize=(length, width), dpi=50)
    ax.set_xlim(0, length)
    ax.set_ylim(0, width)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.grid(which='major', color='#CCCCCC', linestyle='-')
    ax.set_xticklabels("")
    ax.set_yticklabels("")
    
    # this is to add coordinates to each box, this can be used for debugging 
    '''
    for i in np.arange(length+1):
        for j in np.arange(width+1):
            ax.annotate(xy= (i+0.2, j+0.5), text=str(i)+", "+str(j))
   '''         
    return fig, ax

def consecutive(data, stepsize=1):
    '''
    finds consectuive numbers in an array 
    
    Parameters
    ----------
    data: array
        array of numbers 
    stepsize: int
        step size to loop through array
        
    Returns
    -------
    array: array
        array showing where consecutive numbers are in given array
    '''
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)

def get_hint(array): 
    '''
    given an array of 1s and 0s, it returns back grouped hints of where the ones are and how they are grouped 
    
    Parameters
    ----------
    array: array
        array of 0s and 1s
        
    Returns
    -------
    hints: array
        returns back picross hints (number of groups and size of groups) given an array
    '''
    one, = np.where(array == 1)
    np.split(array, np.where(np.diff(array) != 1)[0]+1)
    hints = [len(i) for i in consecutive(one)]
    return hints

def plot_hints(img_array, length, width): 
    '''
    puts hints at the edges of the image 
    
    Parameters
    ----------
    img_array: array
        array containing the image
    length: int
        length of grid to plot image
    width: int
        width of grid to plot image
        
    Returns
    -------
    fig, ax: figure and subplot
        figure with grid plotted by the size given and hints plotted on the sides 
    '''
    
    fig, ax = plot_grid(length, width)
    
    row_hint = []
    column_hint = []

    for i in np.arange(len(img_array)):
        row_hint.append(get_hint(img_array[i]))
        column_hint.append(get_hint(img_array.T[i]))
    
    column_hint = [list(reversed(col)) for col in column_hint] # column hints have to be plotted vertically
    
    # plot rows hints 
    for i in np.arange(1, length+1):
        ax.text(-0.5*len(row_hint[i-1]), i-0.5, ''.join(str(row_hint[i-1]).strip("[]")), fontsize=20)

    # plot columns hints 
    for i in np.arange(1, width+1):
        ax.text(i-.5, width+0.25*len(column_hint[i-1]), str(column_hint[i-1]).strip("[]").replace(",", ",\n"), va='center', fontsize=20)
    
    return fig, ax


