# import the streamlit library
import streamlit as st
 
# give a title to our app
st.title('Welcome to BMI Calculator')
 
hobbies = st.multiselect("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), 'hobbies')
