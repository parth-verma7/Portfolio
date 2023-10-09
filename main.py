import streamlit as st
import pandas as pd 
import numpy as np
import time
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(layout="wide")

st.balloons()
st.snow()

# image = Image.open('mirror-selfie-jawline.jpg')
# st.sidebar.image(image, caption='Sunrise by the mountains', width=250)

col1, col2, col3, col4 = st.columns(4)
with col2:
    url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0bq64Eg5v0spKqJS6nUoUNjD_l02PINnjaVEVgJdSlReN_gCQwKkpk_PONzmJ8EvOEog&usqp=CAU"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((250, 320))
    st.image(img, caption='PARTH VERMA')
    
with col3:
    st.title('Parth Verma')
    st.write("Indian  Institute of  Information Technology, Lucknow")
    st.write("B-Tech : Computer Science and Business '25")
    st.markdown("[Linkedin](https://www.linkedin.com/in/parth-verma-226007228/) - Let's Connect")
    st.markdown("[Github](https://github.com/parth-verma7) - Let's contribute")
    st.markdown("[Twitter](https://twitter.com/v_parth7) - Let's Explore")

# st.header("<h1 style='text-align: center;'>Projects Section</h1>")
st.markdown("<h3 style='text-align: center;'><u>Projects-Section</u></h3>", unsafe_allow_html=True)
st.header("")

col1, col2 = st.columns(2)
with col1:
    image_url="https://miro.medium.com/v2/resize:fit:1400/1*4hCXr7Y6b8vDvQO31il38g.jpeg"
    link_url="https://github.com/parth-verma7/DRONE"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>DRONE MHRD Project</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)
    
with col2:
    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCTUwntPRB_U_l-FGJIYuM0aCdrPy_OvQ6D2AFl5rWFYaSIiKYsw9VqHmZowFuw6UMSpY&usqp=CAU"
    link_url="https://github.com/parth-verma7/MovieRecommendation"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>Hybrid Movie Recommendation System</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)

st.header("")

col1, col2 = st.columns(2)
with col1:
    image_url="https://i.ytimg.com/vi/zACPSbUennk/maxresdefault.jpg"
    link_url="https://github.com/parth-verma7/The-Yoga-Instruct"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>The YOGA Instruct</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)
    
with col2:
    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdpG05KwKrZxem69amzWYoWCDJ3r5xMDFtqw&usqp=CAU"
    link_url="https://github.com/parth-verma7/GestureDetection"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>Gesture Detection Recognition</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)

st.header("")

col1, col2 = st.columns(2)
with col1:
    image_url="https://pbs.twimg.com/media/F2MujqRaIAAFpht?format=jpg&name=small"
    link_url="https://x.com/v_parth7/status/1684934160212017152?s=20"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>Sales Product Dashboard</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)
    
with col2:
    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiyq_OpgvKxxhExayqDyPRlFxdGv3gr283pRvU57ERoriZ3ojYvL190aHTgiotPn-fm8k&usqp=CAU"
    link_url="https://github.com/parth-verma7/LoopHomeInterview"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>Gesture Detection Recognition</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)

st.header("")

col1, col2 = st.columns(2)
with col1:
    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFnTov0m28B7mVlGNvNaPVwAWHLV7m8IeJAPMtTGQzqmOPzyUj17QOaUkRMkwxUM5OWTw&usqp=CAU"
    link_url="https://github.com/parth-verma7/BreatheCV"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>OpenCV Breathing Rate Calculator</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)
    
with col2:
    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhl0ivoG5a7WJJE231UWMo_iF-UmnJEWF66Otu1tMpYBn3_5I_-pWguqJKnrNicqxW5jE&usqp=CAU"
    link_url="https://github.com/parth-verma7/ChatBot"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>NLP Powered Chatbot</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)

st.header("")

col1, col2 = st.columns(2)
with col1:
    image_url="https://img-c.udemycdn.com/course/750x422/5368608_9278_6.jpg"
    link_url="https://github.com/parth-verma7/nextjsembedchain"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>Langchain powered pdf reader</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)
    
with col2:
    image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMIUae5qvtgnCrMxVplWzNMxLMvRCBZUWAW9QFqIidNU00U97WnOW6EAaRc53OBi86eUY&usqp=CAU"
    link_url="https://github.com/parth-verma7/CO2vsElectricVehicles"
    html=f'''
    <div style="text-align:center;">
        <a href="{link_url}" target="_blank">
            <img src="{image_url}" width="{330}" height="{250}">
        </a>
        <p>WHO - CO2 by Electric Vehicles Analysis</p>
    </div>
    '''
    st.markdown(html, unsafe_allow_html=True)