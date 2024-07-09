import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff


df = pd.read_csv("orbit_child.csv")

#chart elements references 

#page configuration setting title and sidebar
st.set_page_config(page_icon="chat2vis.png",layout="wide",page_title="Orbiting Children")
st.markdown("<h1 style='text-align: center; font-weight:bold; font-family:open sans ms; padding-top: 0rem;'> \
            Orbiting Children: Who Are They?</h1>", unsafe_allow_html=True)
#st.sidebar.title("Utilizing Data from AECF/n")
st.sidebar.markdown("Take a look at this to learn more about how current data reports are being written and communicated:https://www.aecf.org/interactive/databook")
#st.sidebar.caption("Utilizing Data from" <a href="datacenter.aecf.org">AECF DataCenter</a>)
st.sidebar.caption("")
st.markdown("Orbiting Children")
# image of a genderless person 
#st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.subheader(" Understanding Identity")

group_labels = ["Time, Amount of Children"]
x = df["TimeFrame_x"]
fig = px.line(df, x= x, y="Num of Child Immigrants")
#ff.create_distplot(df, group_labels)

#fig.show()
st.plotly_chart(fig, use_container_width=True)

st.plotly_chart()
st.plotly_chart()

#container?? 

#container??





#with tab1:
 #   st.plotly_chart(fig, theme="streamlit", use_container_width=True)
#with tab2:
#    st.plotly_chart(fig, theme=None, use_container_width=True)