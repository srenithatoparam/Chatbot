import streamlit as st
import google.generativeai as genai
import os

# Configure your Gemini API key
GOOGLE_API_KEY = "Your_API"
genai.configure(api_key=GOOGLE_API_KEY) 

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    """
    This function sends the user's input to the Gemini model and returns the generated response.
    """
    response = model.generate_content(user_input)
    return response.text

# Streamlit UI setup
st.set_page_config(page_title="Gwen's Chatbot", page_icon="💬")
st.markdown("<h1 style='text-align: center;'>Welcome to Gwen's Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Your AI assistant is here to help you! 🚀</p>", unsafe_allow_html=True)

st.sidebar.header("**Srenitha Toparam**")
st.sidebar.write("Btech in Artificial Intelligence and Data Science")

st.sidebar.header("Contact Information")
st.sidebar.write("Feel free to reach out through the following")
st.sidebar.write("[LinkedIn](www.linkedin.com/in/srenitha-toparam-81a934265)")
st.sidebar.write("[GitHub](https://github.com/srenithatoparam)")
st.sidebar.write("[Email](mailto:srenithatoparam4@gmail.com)")
st.sidebar.write("Developed by Srenitha Toparam", unsafe_allow_html=True)

# Main content area
st.markdown("## Enter your query below:")
user_input = st.text_input("", placeholder="Ask me anything...")

# Add some space for better layout
st.write("")

if user_input:
    with st.spinner("🤔 Thinking..."):
        output = getResponseFromModel(user_input)
    st.markdown("### 🤖 Here is the Gwen's Response:")
    
    # Display the response in a grey-black box with light grey font color
    st.markdown(
        f"<div style='background-color: #2c2f33; padding: 10px; border-radius: 5px; color: #ECECF1;'>{output}</div>",
        unsafe_allow_html=True
    )

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developed by Srenitha Toparam</p>", unsafe_allow_html=True)
