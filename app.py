import streamlit as st
view = [100, 150, 30, 40, 100]

st.write('# test view')
st.write('## raw')
view 
st.write('## bar chart')
st.line_chart(view)
import pandas as pd
sview = pd.Series(view)
sview

st.button('Click me')

import time

with st.spinner(text='In progress'):
    time.sleep(5)
    st.success('Done')0