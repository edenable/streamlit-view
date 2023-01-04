import streamlit as st
view = [100, 150, 30, 40, 100]

st.write('# Youtube view')
st.write('## raw')
view 
st.write('## bar chart')
st.line_chart(view)
import pandas as pd
sview = pd.Series(view)
sview