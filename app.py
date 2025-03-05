import streamlit as st
from openai import OpenAI

OPENAI_API_KEY = ""

st.title("KI Chat")

user_prompt = st.text_input("Deine Anfrage an die KI")

def chat_gpt(user_prompt, model="gpt-4o-mini"):
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model=model,
        store=True,
        messages=[
            {"role": "user", "content": f"{user_prompt}"}
        ],
        stream=True
    )
    return completion
if user_prompt: 
    response = st.write_stream(chat_gpt(user_prompt))


