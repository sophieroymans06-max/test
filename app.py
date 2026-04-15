import streamlit as st
from api import get_gemini_response

# Titel van de app
st.title("Mini Gemini Chatbot")

# Tekstinvoer (prompt)
prompt = st.text_input("Ask something:")

# Knop
if st.button("Send"):
    if prompt:
        response = get_gemini_response(prompt)
        st.write("**Gemini says:**")
        st.write(response)
    else:
        st.write("Please enter a prompt.")
