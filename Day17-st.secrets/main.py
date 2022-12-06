import streamlit as st

st.title('st.secrets')

st.write(st.secrets['message'])
st.write(st.secrets['collection']["message"])