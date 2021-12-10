import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from createpicross import *

## FILE FOR PREVIEWING IMAGES AND GAME STATES
## OPTIONAL TO USE, BUT USEFUL IF YOU WANT TO SEE WHAT YOUR IMAGE WILL LOOK LIKE 
## OR JUST TO CREATE AN ANSWER SHEET FOR YOUR IMAGE 


st.title('PyCross DEMO Viewer')

menu = ["Preview Game", "'Play' Game"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Preview Game":
    st.subheader("Create Game")
    image_file = st.file_uploader("Insert Image", type=["png"])
    if image_file is not None:


        st.image(Image.open(image_file))
        size = st.slider('Size of Window', min_value=5, max_value=50)
        
        make_game = st.checkbox('Show Game')
        show_img = st.checkbox('Show Image')
        play = st.checkbox("Create Game")
        
        if make_game:
            image_array = load_image(img=image_file, window_sizex=size, window_sizey=size)
            length , width = np.shape(image_array)  
            fig, ax = plot_hints(image_array, length, width) 
            st.pyplot(fig)
        if show_img:
            image_array = load_image(img=image_file, window_sizex=size, window_sizey=size)
            fig, ax = plt.subplots()
            ax.imshow(image_array, cmap="Greys")
            st.pyplot(fig)

        if play: 
                st.write('Please enter this sequence of commands after running "python Game.py" into your terminal from the PyCross Folder')
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.write("c")
                    st.write("images/"+str(image_file.name))
                    st.write(str(size))

            
elif choice == "'Play' Game":
    
    st.subheader("Play Game")
    st.session_state.image_array = load_image(img=None)
    
    if 'image_array' not in st.session_state:
        st.session_state['image_array'] = load_image(img=None)
    
    length , width = np.shape(st.session_state.image_array)
    fig, ax = plot_hints(st.session_state.image_array, length, width) 
    st.pyplot(fig)
    play = st.checkbox("Create Game")
    answers = st.checkbox('Show Answers')
    
    if answers: 
        fig, ax = plt.subplots()
        ax.imshow(st.session_state.image_array, origin="lower")
        st.pyplot(fig)


    if play: 
            st.write('Please enter this sequence of commands after running "python Game.py" into your terminal from the PyCross Folder')
            col1, col2, col3 = st.columns(3)
            with col2:
                st.write("p")
        
        
        