import streamlit as st

from agents.planning_assistant import planning_assistant


def show_ai_assistant(farmer_details, result):

    st.divider()

    st.markdown("## 🌱 AI Planning Assistant")

    st.info(
        "You can ask any question about the generated cultivation plan."
    )

    if "assistant_messages" not in st.session_state:
        st.session_state.assistant_messages = []

    # Display previous conversation
    for message in st.session_state.assistant_messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    question = st.chat_input(
        "Ask about your cultivation plan..."
    )

    if question:

        # Save User Message
        st.session_state.assistant_messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                answer = planning_assistant(
                    farmer_details,
                    result,
                    question
                )

                st.markdown(answer)

        # Save AI Message
        st.session_state.assistant_messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )