
#import 
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

#chart elements references 
'''
'''
#page configuration setting title and sidebar
st.set_page_config(page_icon="chat2vis.png",layout="wide",page_title="Orbiting Children")
st.markdown("<h1 style='text-align: center; font-weight:bold; font-family:open sans ms; padding-top: 0rem;'> \
            Orbiting Children: Who Are They?</h1>", unsafe_allow_html=True)
st.sidebar.title("Utilizing Data from AECF/n")
st.sidebar.markdown
#st.sidebar.caption("Utilizing Data from" <a href="datacenter.aecf.org">AECF DataCenter</a>)



st.subheader("<style font-family:> Understanding Identity</style>")
df = px.data.iris()
fig = px.scatter()
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Demographics", ""])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)