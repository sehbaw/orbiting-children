
#ok none of this code is usuable because I cannot get gsheet connection working!!! commenting it out so perhaps i can return to it later

import streamlit as st
import pandas as pd

col1,col2, col3 = st.columns(3)

with st.sidebar: 
    st.title("Learn more about the Data")
    st.write('Annie E Casey Foundation is a nonprofit organization\nfocused on improving te lives of children in relation to their educational, economic, social and health outcomes')
    


with st.container:
    st.text("Interesectionality aims to discuss the various mix of identities that may not always be represented. ")
with col1:
    


with col2:
    



with col3: 


















#from streamlit_gsheets import GSheetsConnection

#url = "https://docs.google.com/spreadsheets/d/1yBogRIScP19gdB83WGb3hiczHEjiyX_E3D3GQzlp5tg/edit?usp=sharin"
# Create a connection object.
#conn = st.connection("gsheets", type=GSheetsConnection)

#df = conn.read(
#    worksheet=url,
#    ttl="10m",
#    usecols=[0, 1],
#    nrows=3,
#)

# Print results.
#for row in df.itertuples():
 #   st.write(f"{row.name}")

#st.set_page_config(page_icon="chat2vis.png",layout="wide",page_title="Orbiting Children")
#st.markdown("<h1 style='text-align: center; font-weight:bold; font-family:open sans ms; padding-top: 0rem;'> \
 #           Orbiting Children: Who Are They?</h1>", unsafe_allow_html=True)


#st.sidebar.markdown("Utilizing Data from AECF")
#st.sidebar.markdown()
#st.sidebar.caption("Utilizing Data from" <a href="datacenter.aecf.org">AECF DataCenter</a>)

#for row in df.itertuples():
 #   st.write(f"{row.name} has a :{row.pet}:")
#df = conn.read(
 #   worksheet="Sheet1",
 #   ttl="10m",
  #  usecols=[0, 1],
  #  nrows=3,
#)


#else:
    # use the list already loaded

    #datasets = st.session_state["datasets"]

    # Radio buttons for dataset choice
#chosen_dataset = chosen_dataset.radio(":bar_chart: Choose your data:",datasets.keys(),index=index_no)#,horizontal=True,)