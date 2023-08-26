import streamlit as st
import pandas as pd 
import numpy as np
import time
from PIL import Image

st.balloons()
st.snow()

# image = Image.open('mirror-selfie-jawline.jpg')
# st.sidebar.image(image, caption='Sunrise by the mountains', width=250)

col1, col2 = st.columns(2)
with col1:
    # image = Image.open('mirror-selfie-jawline.jpg')
    url="https://github.com/parth-verma7/Portfolio/blob/main/mirror-selfie-jawline.jpg?raw=true"
    st.image(url, caption='PARTH VERMA', width=250)
    
with col2:
    st.title('Parth Verma')
    st.write("Indian  Institute of  Information Technology, Lucknow")
    st.write("B-Tech : Computer Science and Business '25")
    st.markdown("[Linkedin](https://www.linkedin.com/in/parth-verma-226007228/) - Let's Connect")
    st.markdown("[Github](https://github.com/parth-verma7) - Let's contribute")
    st.markdown("[Twitter](https://twitter.com/v_parth7) - Let's Follow")



# "Hello, world!"
# # st.write("Hello, world!")
# df=pd.DataFrame({'name':['Parth', 'Verma'], 'Number':[7,9]})
# st.write(df)
# # st.table(df)
# st.dataframe(df)

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
# st.line_chart(chart_data)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.map(map_data)

# x = st.slider('x')
# st.write(x, 'squared is', x * x)

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])
#     # st.dataframe(chart_data)
#     chart_data

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })
# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])
# 'You selected: ', option

# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# left_column, right_column = st.columns(2)
# left_column.button('Press me!')
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(2)

