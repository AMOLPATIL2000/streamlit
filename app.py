# import the streamlit library
import streamlit as st
 
# give a title to our app
st.title('Welcome to BMI Calculator')
level = st.slider("Select the level", 1, 5)
# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))
