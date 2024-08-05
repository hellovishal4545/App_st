import streamlit as st
import pyshorteners as pyst
shortner = pyst.Shortener()
import pyperclip
def copying():
    pyperclip.copy(shorted_url)
    
st.markdown("<h1 style = 'text-align:center;> URL Shortner</h1>",unsafe_allow_html=True)
form = st.form("name")
url = form.text_input('URL here')
s_btn = form.form_submit_button("Search")
if s_btn:
    shorted_url = shortner.tinyurl.short(url)
    #print(shorted_url)
    st.markdown('<h3>SHORTED URL</h3>',unsafe_allow_html=True)
    st.markdown(f"<h6 style ='text-align:center;'> {shorted_url}</h6>",unsafe_allow_html=True)
    st.button('Copy',on_click=copying)  #calling a fun ->> copying
           