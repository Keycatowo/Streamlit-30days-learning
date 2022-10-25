import streamlit as st

st.header('Day03-學習BUtton')

if st.button('Say Hello'):
    st.write("Hello")
else:
    st.write("Bye")