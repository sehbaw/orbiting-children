import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


#df = pd.read_csv("orbit_child.csv")

#chart elements references 

#page configuration setting title and sidebar
st.set_page_config(page_icon="chat2vis.png",layout="wide",page_title="Orbiting Children")
st.markdown("<h1 style='text-align: center; font-weight:bold; font-family:open sans ms; padding-top: 0rem;'> \
            Orbiting Children: Who Are They?</h1>", unsafe_allow_html=True)
#st.sidebar.title("Utilizing Data from AECF/n")
st.sidebar.markdown("Take a look at this to learn more about how current data reports are being written and communicated:https://www.aecf.org/interactive/databook")
#st.sidebar.caption("Utilizing Data from" <a href="datacenter.aecf.org">AECF DataCenter</a>)
st.markdown("Orbiting Children")
# image of a genderless person 
#st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.subheader("Understanding Identity")

st.write("When thinking about what foster kids have and don't have, there is a lot to cover.")
st.sidebar.markdown('''Based on what the Annie E. Casey Foundation has come together to produce, there were about six factors
         that impact the identity and existence of foster youth''')

         #insert image here
st.image("imgs\intersectionality.svg")


##exploring age!! sunburst? 1..1.2


st.write('''When working at CASA, my project  the topic that we tended to come across the most: education.
How many kids are getting an education? Is school considered a priority? How can present a way to get them engaged
         towards graduating and pursuing a career (that does not necessarily mean college)
         ''')

df_age = pd.read_excel('data\Child population by age group.xlsx')
df_filter = df_age[(df_age['TimeFrame'] >= 2019) & (df_age['TimeFrame'] <= 2022) & (df_age['DataFormat'] == 'Number')]
#filtered_df = df_filter.loc[~df_filter['Age group '] != "Total less than 18"] # .loc is not in-place replacement
filtered_df = df_filter.loc[df_filter['Age group'] != "Total less than 18"]


#ages = df_age[df_age['DataFormat'] == 'Percent' && df_age['Data']]
#ages = df_filter[df_filter['DataFormat'].apply(lambda x: isinstance(x, float))]

# Create pie chart for percentages
fig_percent = px.pie(
       df_filter,
        names='Age group',
        values= df_filter['Data'],
        title=f'Age Group Percentages from 2019 to 2022'
    )
st.plotly_chart(fig_percent)


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['education','health','housing','economic well-being','employment','family & community'])























#labels = df_age['Age group']
#values = ages
'''fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo = 'label+percent',
                       insidetextorientation='radial'              
                             )])'''

#ff.create_distplot(df, group_labels)
#st.menu()
#fig.show()
#st.write('''some things to think about when discussing identity in foster youth is to examine the typical groups experiencing 
      #    ''')
# education
#st.write('Understanding education wihtin foster youth is vital')
#with st.container():
#    with tab1: 
 #       st.plotly_chart(fig, use_container_width=True