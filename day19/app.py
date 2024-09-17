#pip install streamlit
#to run write this in terminal - streamlit run app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#set path plotting backend to plotly
pd.options.plotting.backend='plotly'

@st.cache_data
def load_database():
    return pd.read_csv("Data Sets/canada_clean.csv")

st.title("Canada Immigration Analysis")

with st.spinner("Loading Data..."):
    df=load_database()
    
with st.expander("Show Dataset"):
    st.dataframe(df)

countrylist=df['Country']
selected_country=st.selectbox("Select a Country",countrylist)
min_yr,max_yr=st.slider("Select years",min_value=1980,max_value=2013,value=(1980,2013))
st.header(f"Country: {selected_country}")
df=df.set_index('Country')
country=df.loc[selected_country,str(min_yr):str(max_yr)]
fig=country.plot()
st.plotly_chart(fig)
