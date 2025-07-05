import streamlit as st

st.title("안녕하세요! ☺")
name = st.text_input("이름을 입력하세요")
if name:
    st.write(f"{name} 님, Streamlit 첫 데모에 오신 것을 환영합니다!")
