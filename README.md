# PyCross
Picross in Python 

To start, please download the main "PyCross" Folder and go to the folder via the Terminal.

Once your inside the folder through the terminal, Enter: 

```
python Game.py
```

Note: Please make sure the images file is correctly downloaded in order to start the program. This is to ensure that there you will still be able to play the game even if you do not provide the program an image. Thanks! 

**If you wish to use your own custom image, please insert them into the images folder to use.**


## **To Play a Game:**
1. Once you've run Game.py in Terminal and you should be prompted with: 
```
Would you like to create or play a game? (Enter 'c' or 'p')
```
Please enter 'p' and you will recieve a random image to play, ranging in difficulty. 


## **To Create a Game:**
1. Once you've run Game.py in Terminal and you should be prompted with: 
```
Would you like to create or play a game? (Enter 'c' or 'p')
```
2. If you wish to create your own picross game, please insert a filepath to your image (size max: 100KB). There are some images already provided, if you wish to use them, please type: 
```
images/imagename.png
```
4. You will be asked for a window size: 
```
Window Size?
```
TIP: For easy: 10, medium: 20, hard: 25, extreme: 30. Please be advised that the bigger your size, the more cluttered your screen will be. 

Have FUN! 

## Using Demo.py
Please Demo.py if you wish to preview what your image will look like in the game or to create an answer sheet for your image. Some images, particularlly images of larger size or of more detail may not look good as a game. Use Demo.py to check out how the game will look. To run, you will need streamlit: 
```
streamlit run Demo.py
```
