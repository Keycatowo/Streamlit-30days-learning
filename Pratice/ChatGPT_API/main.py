import streamlit as st
import requests

st.title("ChatGPT API 測試")

st.sidebar.title("API KEY")
api_key = st.sidebar.text_input("Your API KEY", value="")

response_model = requests.get(
    url = "https://api.openai.com/v1/models",
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
)

with st.expander("Response Model"):
    st.write(response_model.json())
    st.markdown("正常結果樣子:![](https://i.imgur.com/9OorANT.png)")

with st.form("測試文字"):
    st.subheader("輸入文字")
    text = st.text_input("輸入文字", value="Say this is a test")
    submit = st.form_submit_button("送出")

if submit:
    st.write("送出文字:", text)
    response_text = requests.post(
        url = "https://api.openai.com/v1/completions",
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": text,
            "max_tokens": 100,
            "temperature": 0.9,
            "model": "text-davinci-003"
        }
    )
    st.write(response_text.json())
    st.markdown("正常結果樣子:![](https://i.imgur.com/cyxsVaE.png)")
