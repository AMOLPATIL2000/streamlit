# import the streamlit library
import streamlit as st
 
# give a title to our app
st.title('Welcome to BMI Calculator')
 
hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)
