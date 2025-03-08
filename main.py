import streamlit as st
from openai import OpenAI

from conversations import Conversation
from llm import LLM, LLMName

st.title("Medical Diagnosis POC")

if "llm" not in st.session_state:
    llm: LLM = LLM(model_name=LLMName.LLAMA_3_1_8B_TURBO)
    st.session_state["llm"] = llm
else:
    llm: LLM = st.session_state.llm

if "convo" not in st.session_state:
    convo: Conversation = Conversation()
    st.session_state.convo = convo
else:
    convo: Conversation = st.session_state.convo

for message in convo.messages:
    with st.chat_message(message.role):
        st.markdown(message.content)

if user_message := st.chat_input("Type a message..."):
    convo.add_user_message(user_message)
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        llm: LLM = st.session_state.llm
        response = llm.generate(convo)
        st.markdown(response)
    convo.add_assistant_message(response)
    st.session_state.convo = convo