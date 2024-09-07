import streamlit as st
import base64

# Ensure the user is logged in
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning("Please log in to access the Home page.")
    st.stop()  


st.title("Welcome to the Home Page!")
st.write("This content is only available after logging in.")
def set_background_image(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with the local image path
set_background_image("/Users/raakin/Desktop/apigwtest/2022-Formula1-Ferrari-F1-75-003-1440w.jpg")
