# plotly + streamlit

## Scatter
```python
df = px.data.iris()
st.write(px.scatter(df, x='sepal_width', y='sepal_length', color='species'))
```
![scatter](../../fig/Streamlit%2Bplotly-scatter%E7%AF%84%E4%BE%8B.png)

