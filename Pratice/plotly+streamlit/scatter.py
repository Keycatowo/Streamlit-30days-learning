#%%
import streamlit as st
import plotly.express as px

st.title('📊 Plotly Express App')


df = px.data.iris()

st.write('## Iris Dataset')
st.write(df)

st.write('## Scatter Plot')
st.write(px.scatter(df, x='sepal_width', y='sepal_length', color='species'))
