import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import numpy as np

### Config
st.set_page_config(
    page_title="Crossfit",
    page_icon="🏋️‍♂️ ",
    layout="wide"
)

st.title("Build dashboards with Streamlit 🎨")

st.markdown("""
Details on the athletes participating in the 2020 Crossfit OPENS
""")

DATA_URL = '2020_opens_athletes.csv'

def load_data(nrows=''):
    if(nrows == ''):
        return pd.read_csv(DATA_URL,low_memory=False)
    else:
        return pd.read_csv(DATA_URL,nrows=nrows)
          

# Load all data
data = load_data()
mask = (data['is_scaled'] < 1) # Only RX Athlete 
data_with_filter = data[mask]

# Preview
st.write(load_data(100))

nRow, nCol = data_with_filter.shape
st.markdown(f'The file 2020_opens_athletes.csv has {nRow} rows (RX Athlete) and {nCol} columns.')

st.info('🚨 Small precision on the data, I kept only the athletes in RX. (For all the visualizations that are below)')


st.markdown('**💥 Number of participants per country.**')

fig = px.histogram(data_with_filter.sort_values("countryoforiginname"), x="countryoforiginname", barmode="group")
st.plotly_chart(fig, use_container_width=True)


#### Create two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("**1️⃣ Division by Gender**")
    country = st.selectbox("Select a country", data_with_filter["countryoforiginname"].sort_values().unique())
    
    country_sales = data_with_filter[data_with_filter["countryoforiginname"]==country]

    fig = px.histogram(country_sales, x="gender", color="division")
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown(f"**2️⃣ Average on age, height and weight in {country}**")
    
    division = st.selectbox("Select a division",data_with_filter["division"].sort_values().unique())

    avg_age_height = data_with_filter[((data_with_filter["countryoforiginname"]==country) & (data_with_filter["division"]==division))]

    avg = avg_age_height.mean()
    st.metric("Average age:", np.round(avg['age'], 2))
    st.metric("Average height(m):",np.round(avg['height'], 2))
    st.metric("Average weight(kg):",np.round(avg['weight'], 2))
    st.metric("Average IMC:",np.round(avg['weight'] /  (avg['height']**2),2))


st.markdown(f"**3️⃣ Affiliate Box in {country}**")

country_sales = data_with_filter[(data_with_filter["countryoforiginname"]==country)] #  & (np.sum(data_with_filter["affiliatename"])>100)
fig = px.histogram(country_sales, x="affiliatename",nbins=100)
fig.update_layout(bargap=0.2)
st.plotly_chart(fig, use_container_width=True)