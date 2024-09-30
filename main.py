import streamlit as st
from groq import Groq

#initialize the api_key
client = Groq(api_key='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')


#create a function
def get_groq_response(user_input):
    completion = client.chat.completions.create(
    model="llama-3.2-3b-preview",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

    response_text = ""
    for chunks in completion:
        response_text += chunks.choices[0].delta.content or ""
    return response_text

#streamlit app layout
st.title("Llama 3.2 Chatbot")
st.write("This web app will interact with Llama 3.2 llm model to generate the response")


#input the text
user_input = st.text_input("Enter your message : ")

#when the user clicks the button then, get the response from the groq
if st.button('Send'):
    with st.spinner("Generating Response..."):
        response = get_groq_response(user_input)

    st.success("response received.!")
    st.write(response)
st.markdown("***Lavish Gangwani***", unsafe_allow_html=True)
