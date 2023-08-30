

import streamlit as st
import pandas as pd
st.set_page_config(page_icon="chat2vis.png",layout="wide",page_title="Orbiting Children")
st.markdown("<h1 style='text-align: center; font-weight:bold; font-family:open sans ms; padding-top: 0rem;'> \
            Orbiting Children: Who Are They?</h1>", unsafe_allow_html=True)


st.sidebar.markdown("Utilizing Data from AECF/n")
#st.sidebar.caption("Utilizing Data from" <a href="datacenter.aecf.org">AECF DataCenter</a>)



#else:
    # use the list already loaded

    #datasets = st.session_state["datasets"]

    # Radio buttons for dataset choice
chosen_dataset = chosen_dataset.radio(":bar_chart: Choose your data:",datasets.keys(),index=index_no)#,horizontal=True,)