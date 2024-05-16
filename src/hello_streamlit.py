import streamlit as st

st.header("The amazing YouTube video of a cave", anchor="Cave", 
          help="There is no one coming to help you in a cave. Help yourself", divider=False)
st.subheader("(c) Rahul Swaminathan", anchor = None, help = None, divider = True)
st.text("A really cool cave in Sardegna thats tight, loops under itself \n and beautiful to navigate inside")


youtube_url = "https://youtu.be/YTlhaPGLY68"  
st.video(youtube_url)

