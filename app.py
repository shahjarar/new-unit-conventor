import streamlit as st
from pint import UnitRegistry

# Pint Library Initialization
ureg = UnitRegistry()

st.set_page_config(page_title="Unit Converter Chatbot 🤖")

# **Step 1: Show Title at the Top**
st.title("🔄 Unit Converter Chatbot 🤖")

# **Step 2: Ask for User Name**
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.user_name:
    st.session_state.user_name = st.text_input("Enter your name to start:")

# **Step 3: Show Welcome Message After Name is Entered**
if st.session_state.user_name:
    st.subheader(f"👋 Welcome, {st.session_state.user_name}!")
    st.write("Hello! I'm a chatbot that can help you convert units. 📏🌡️🏋️‍♂️")
    st.write("Ask me to convert any unit, like: 'Convert 10 kg to pounds'")

    # **Step 4: Initialize Chat History**
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    user_input = st.chat_input("Type your conversion query...")

    def convert_units(amount, from_unit, to_unit):
        """Unit conversion function using Pint Library"""
        try:
            result = amount * ureg(from_unit).to(to_unit)
            return f"{amount} {from_unit} = {result}"
        except:
            return "❌ Invalid units! Try again."

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Extract conversion request
        words = user_input.lower().split()
        try:
            amount = float(words[1])
            from_unit = words[2]
            to_unit = words[-1]
            bot_reply = convert_units(amount, from_unit, to_unit)
        except:
            bot_reply = "❌ Please enter in this format: 'Convert 10 kg to pounds'"

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        with st.chat_message("assistant"):
            st.markdown(bot_reply)