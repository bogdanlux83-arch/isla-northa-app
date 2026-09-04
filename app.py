import streamlit as st
import pandas as pd

#add a title to the app
st.title("My First Streamlit App")

#add a header
st.header("IslaNortha")

#add a text
st.write("possible i could do something here.... this is gonna be my first ever apps and then connect it to my custom dinosaur game isla northa, first ever one to be honest. other than POT(Path of Titans), but u may be abled to navigate through the app as it were any other existing app. Isla northa is a custom dinosaur game that i am working on and i am gonna connect it to this app. This app will be abled to take you to the isla northa website to then purchase the game, download, or to then view the website of IslaNortha.com. --------")
st.write("I  S  L  A  N  O  R  T  H  A")
st.write("█  ▀  █  █▄█ █▄█ █▄█ █▀▄  █  █▀█ █▄█")
st.write("█ ▄▄  █▄ █ █ █ ▀ █▄█ █ █  █  █ █ █ █")

gradient_html = """
<span style="background: linear-gradient(90deg, #FF4B4B, #24963F); 
             color: white; padding: 4px 12px; font-weight: bold; border-radius: 4px;">
    ------ISLANORTHA-------
    -------I S L A N O R T H A-------
    --------Isla northa-------
</span>
"""
st.markdown(gradient_html, unsafe_allow_html=True)

#add your credentials here
#For Demo purposes we will not use a database, we will use a dictionary in the session state.
st.write("For Demo purposes we will not Store your Credentials.")
if "users" not in st.session_state:
    #demo
    st.session_state.users = {"admin": "admin"}
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

tab_login, tab_signup = st.tabs(["Login", "Signup"])

with tab_login:
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login")
        if login_username in st.session_state.users and st.session_state.users[login_username] == login_password:
            st.session_state.logged_in_user = login_username
            st.success(f"Welcome back, {login_username}!")
        else:
            st.error("Invalid username or password")

with tab_signup:
    signup_username = st.text_input("Username", key="signup_username")
    signup_password = st.text_input("Password", type="password", key="signup_password")
    if st.button("Create Account")
        if not new_user or not new_password:
            st.warning("Please enter a username and password")
        elif new_user in st.session_state_users:
            st.error("Username already exists")
        else:
            st.session_state.users[new_user] = new_password
            st.success(f"Account created succesfully for {new_user}!")

if st.session_state.logged_in_user:
    st.write(f"Logged in as **{sg.session_state.logged_in_user}**")

#Interactive widget: text input
user_input = st.text_input("Enter your name")
st.write(f"Hello, **{user_input}**!")

#Play With The Slider
gradient_html = """
<span style="background: linear-gradient(90deg, #FF4B4B, #24963F); 
             color: white; padding: 4px 12px; font-weight: bold; border-radius: 4px;">
    Play With The Slider If Your Bored.
</span>
"""
st.markdown(gradient_html, unsafe_allow_html=True)

#Interactive widget: slider
num = st.slider("Select a number from 1 to 10", 1, 10, 5)
st.write(f"The square of **{num}** is **{num**2}**")


# Links
st.subheader("Links")
STREAMLIT_APP_URL = "https://isla-northa-app-j4mue7kjwk5rscctd7cunc.streamlit.app"
st.link_button("Isla Northa website", "https://islanortha.com")
st.link_button("Open this Streamlit app", STREAMLIT_APP_URL)

# Vote: Isla Northa vs The Isle
st.subheader("Which is better?")
st.write("Vote for your favourite dinosaur game on the official page:")

VOTE_SITE_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfExMRSUYEYhXTcqv2XV0kTY7VcyIS6I3ow1_OWpSAyzyb7Rg/viewform?usp=publish-editor"
st.link_button("Open official vote page", VOTE_SITE_URL)

#add a footer
st.markdown(
    """
    <div style='text-align:center; color:gray;'>
      Copyright 2026 Isla Northa. All rights reserved.<br>
      <a href="https://islanortha.com/terms" target="_blank">Terms of Service</a> ·
      <a href="https://islanortha.com/privacy" target="_blank">Privacy Policy</a> ·
      <a href="https://islanortha.com/cookies" target="_blank">Cookie Policy</a>
    </div>
    """,
    unsafe_allow_html=True,
)