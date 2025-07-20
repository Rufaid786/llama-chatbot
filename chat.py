import streamlit as st
import ollama as ollama

def generate_llm_response(query,model='llama3.2'):

    message=[
        {
            'role':'user',
            'content': query
        }
    ]
    response=ollama.chat(model=model,messages=message)
    return response['message']['content']

st.title('LLM Text Generator')
st.text('A sample LLM chatbot developed using ollam3.2')

user_input=st.text_area("Enter your input:")

if st.button('Get an answer :'):
    if user_input.strip()!="":
        with st.spinner("Taking a look:"):
            try:
                llm_response=generate_llm_response(user_input)
                st.success('Response generated')
                st.text_area("LLM response:",value=llm_response,height=250)
            except Exception as e:    
                st.error(f"Error occured {e}")

    else:
        st.warning("Please enter a prompt")        
