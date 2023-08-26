import streamlit as st
import pandas as pd 
import numpy as np
import time
import requests
from PIL import Image
from io import BytesIO

# st.set_page_config(layout="wide")

st.balloons()
st.snow()

# image = Image.open('mirror-selfie-jawline.jpg')
# st.sidebar.image(image, caption='Sunrise by the mountains', width=250)

col1, col2 = st.columns(2)
with col1:
    url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0bq64Eg5v0spKqJS6nUoUNjD_l02PINnjaVEVgJdSlReN_gCQwKkpk_PONzmJ8EvOEog&usqp=CAU"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((250, 320))
    st.image(img, caption='PARTH VERMA')
    
with col2:
    st.title('Parth Verma')
    st.write("Indian  Institute of  Information Technology, Lucknow")
    st.write("B-Tech : Computer Science and Business '25")
    st.markdown("[Linkedin](https://www.linkedin.com/in/parth-verma-226007228/) - Let's Connect")
    st.markdown("[Github](https://github.com/parth-verma7) - Let's contribute")
    st.markdown("[Twitter](https://twitter.com/v_parth7) - Let's Explore")

# st.header("<h1 style='text-align: center;'>Projects Section</h1>")
st.markdown("<h3 style='text-align: center;'>Projects Section</h3>", unsafe_allow_html=True)
st.header("")

col1, col2 = st.columns(2)
with col1:
    image_url="https://miro.medium.com/v2/resize:fit:1400/1*4hCXr7Y6b8vDvQO31il38g.jpeg"
    link_url="https://github.com/parth-verma7/DRONE"
    st.markdown(f'<div style="text-align:center;"><a href="{link_url}" target="_blank"><img src="{image_url}" width="{330}" height="{250}">DRONE WCARL Project</a>', unsafe_allow_html=True)
    
with col2:
    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCTUwntPRB_U_l-FGJIYuM0aCdrPy_OvQ6D2AFl5rWFYaSIiKYsw9VqHmZowFuw6UMSpY&usqp=CAU"
    link_url="https://github.com/parth-verma7/MovieRecommendation"
    st.markdown(f'<div style="text-align:center;"><a href="{link_url}" target="_blank"><img src="{image_url}" width="{330}" height="{250}">Hybrid Moview Recommendation System</a>', unsafe_allow_html=True)

st.header("")

col1, col2 = st.columns(2)
with col1:
    image_url="https://i.ytimg.com/vi/zACPSbUennk/maxresdefault.jpg"
    link_url="https://github.com/parth-verma7/The-Yoga-Instruct"
    st.markdown(f'<div style="text-align:center;"><a href="{link_url}" target="_blank"><img src="{image_url}" width="{330}" height="{250}">The YOGA Instruct</a>', unsafe_allow_html=True)
    
with col2:
    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdpG05KwKrZxem69amzWYoWCDJ3r5xMDFtqw&usqp=CAU"
    link_url="https://github.com/parth-verma7/GestureDetection"
    st.markdown(f'<div style="text-align:center;"><a href="{link_url}" target="_blank"><img src="{image_url}" width="{330}" height="{250}">Gesture Detection Recognition</a>', unsafe_allow_html=True)