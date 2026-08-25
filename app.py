import streamlit as st
import pandas as pd

#add a title to the app
st.title("My First Streamlit App")

#add a header
st.header("IslaNortha")

#add a text
st.write("possible i could do something here.... this is gonna be my first ever apps and then connect it to my custom dinosaur game isla northa, first ever one to be honest. other than POT(Path of Titans), but u may be abled to navigate through the app as it were any other existing app. Isla northa is a custom dinosaur game that i am working on and i am gonna connect it to this app. This app will be abled to take you to the isla northa website to then purchase or view the website of IslaNortha.com. --------")
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

#Interactive widget: slider
num = st.slider("Select a number from 1 to 10", 1, 10, 5)
st.write(f"The square of **{num}** is **{num**2}**")

#Display a dataframe
st.subheader("Sample DataFrame")
df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5],
    'col2': [10, 20, 30, 40, 50]
    
})
st.dataframe(df)

#Interactive widget: button
if st.button("Isla Northa.com"):
    st.link_button("Here is the link to Isla Northa.com", "https://islanortha.com")
    st.success("Taking you to Isla Northa.com!")

# Vote: Isla Northa vs The Isle
st.subheader("Which is better?")
st.write("Vote for your favourite dinosaur game on the official page:")

# Put your real website/form URL here when you have one
VOTE_SITE_URL = "https://forms.gle/YOUR_FORM_ID"
st.link_button("Open official vote page", VOTE_SITE_URL)

#add a footer
st.markdown(
    "<div style='text-align:center; color:gray;'>copyright 2026 Isla Northa. All rights reserved.</div>",
    unsafe_allow_html=True,
)