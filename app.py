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
username = st.text_input("Enter your username")
password = st.text_input("Enter your password", type="password")
if st.button("Login"):
    if username == "admin" and password == "admin":
        st.success("Login successful")
    else:
        st.error("Invalid username or password")

#Interactive widget: text input
user_input = st.text_input("Enter your name")
st.write(f"Hello, **{user_input}**!")

#Play With The Slider
st.write("Play With The Slider If Your Bored.")
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