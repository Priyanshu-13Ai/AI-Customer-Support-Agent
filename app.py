import streamlit as st
import os
from dotenv import load_dotenv

from agent import run_agent

# Ensure environment variables are loaded
load_dotenv()

st.set_page_config(page_title="AI Customer Support Agent", page_icon="🤖")

st.title("🤖 Customer Support Agent")
st.markdown("Ask me anything about your orders or our products!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("E.g., Where is order ORD-1002?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Check if API key is set
    if not os.getenv("GROQ_API_KEY"):
        response = "Please set your GROQ_API_KEY environment variable to use the agent."
    else:
        with st.spinner("Thinking..."):
            # Pass everything *before* this new user turn as history so the
            # agent can resolve follow-ups like "1002" in context.
            history = st.session_state.messages[:-1]
            response = run_agent(prompt, chat_history=history)
            
    
    with st.chat_message("assistant"):
        st.markdown(response)
        
    
    st.session_state.messages.append({"role": "assistant", "content": response})