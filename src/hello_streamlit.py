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


import http
import pandas as pd

# /Users/srahul/Documents/Work/git_repo/streamlit_20240516/data/01_raw/PSCompPars_2023.09.06_16.02.03.csv
url = "/Users/srahul/Documents/Work/git_repo/streamlit_20240516/data/01_raw/PSCompPars_2023.09.06_16.02.03.csv"
url = st.text_input('The URL link')

if url:
    dfin = pd.read_csv(url)  # read a CSV file  from given URL
    df = dfin.query("hostname=='11 Com'")
    st.write(df)

    st.scatter_chart(df, x="pl_rade", y = "pl_bmasse", color = "st_teff", size ="st_rad")

# querystr = "hostname == " +  dfin['hostname'][0]
#     df = dfin.query(querystr)