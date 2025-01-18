# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# import streamlit as st

# def get_googleai_response(question):
#   llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.9)
#   response = llm.invoke(question)  # Use invoke instead of __call__
#   return response

# # Using Streamlit

# st.set_page_config(page_title="Q & A Chatbot", page_icon=":robot_face:")

# st.header("langchain Q & A Chatbot")

# user_input = st.text_input("Input:", key="input")
# response = get_googleai_response(user_input)  # Call with user input

# submit = st.button("Ask the question")

# if submit:
#   st.subheader("The Response is")
#   st.write(response.content)  # Access the content attribute of the response

  # For deployment on hugging face spaces add your API key in secrets and change the above code as this:

import os
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

def get_googleai_response(question):
    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. Please add it to your secrets.")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.9, google_api_key=google_api_key)
    response = llm.invoke(question)
    return response

# Streamlit app
st.set_page_config(page_title="Q & A Chatbot", page_icon=":robot_face:")
st.header("LangChain Q & A Chatbot")

user_input = st.text_input("Input:", key="input")

submit = st.button("Ask the question")

if submit:
    if not user_input:
        st.warning("Please enter a question.")
    else:
        try:
            response = get_googleai_response(user_input)
            st.subheader("The Response is")
            st.write(response.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")