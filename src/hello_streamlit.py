import streamlit as st

st.header("An amazing YouTube video of a cave", anchor="Cave", 
          help="There is no one coming to help you in a cave. Help yourself", divider=False)
st.subheader("(c) Rahul Swaminathan", anchor = None, help = None, divider = True)
st.text("A really cool cave in Sardegna thats tight, loops under itself \n and beautiful to navigate inside")

with st.sidebar:
    choice = st.radio("Choose a video",
        ("Groto del Fico", 
         "Molnar Janos")
    )

if(choice=="Groto del Fico"):
    youtube_url = "https://youtu.be/YTlhaPGLY68"
else:
    youtube_url = "https://youtu.be/9VPt8MvPLm0"

st.video(youtube_url)
