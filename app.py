# import streamlit as st
# from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text
# from audio_recorder_streamlit import audio_recorder
# from streamlit_float import *

# # Initialize floating features for the interface
# float_init()

# # Initialize session state for managing chat messages
# def initialize_session_state():
#     if "messages" not in st.session_state:
#         st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I assist you today?"}]

# initialize_session_state()

# st.title("OpenAI Conversational Chatbot 🤖")

# # Create a container for the microphone and audio recording
# footer_container = st.container()
# with footer_container:
#     audio_bytes = audio_recorder()

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# if audio_bytes:
#     with st.spinner("Transcribing..."):
#         # Write the audio bytes to a temporary file
#         webm_file_path = "temp_audio.mp3"
#         with open(webm_file_path, "wb") as f:
#             f.write(audio_bytes)

#         # Convert the audio to text using the speech_to_text function
#         transcript = speech_to_text(webm_file_path)
#         if transcript:
#             st.session_state.messages.append({"role": "user", "content": transcript})
#             with st.chat_message("user"):
#                 st.write(transcript)
#             os.remove(webm_file_path)


# if st.session_state.messages[-1]["role"] != "assistant":
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking🤔..."):
#             final_response = get_answer(st.session_state.messages)
#         with st.spinner("Generating audio response..."):    
#             audio_file = text_to_speech(final_response)
#             autoplay_audio(audio_file)
#         st.write(final_response)
#         st.session_state.messages.append({"role": "assistant", "content": final_response})
#         os.remove(audio_file)

# footer_container.float("bottom: 0rem;")

import os
import streamlit as st
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text
from audio_recorder_streamlit import audio_recorder
from streamlit_float import float_init

st.markdown("""
    <style>
        .block-container {
            padding-top: 0.5rem !important;
        }
        h1 {
            margin-top: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize floating UI
float_init()


# Initialize session state
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I assist you today?"}
        ]


initialize_session_state()

st.title("OpenAI Conversational Chatbot using gpt-5-nano-2025-08-07")


# # Recording container
# footer_container = st.container()
# with footer_container:
#     audio_bytes = audio_recorder()
#     user_text = st.text_input("Type your message:", key="footer_input")

# Recording + Text Box Footer
footer_container = st.container()

with footer_container:
    col1, col2 = st.columns([4, 1])   # Adjust width ratio as needed

    with col1:
        user_text = st.text_input(
            "",
            placeholder="Type your message...",
            key="footer_input",
            label_visibility="collapsed"
        )

    with col2:
        audio_bytes = audio_recorder()

# Show conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# If audio was recorded
if audio_bytes:
    with st.spinner("Transcribing..."):
        temp_path = "temp_audio.mp3"
        with open(temp_path, "wb") as f:
            f.write(audio_bytes)

        transcript = speech_to_text(temp_path)

        if transcript:
            st.session_state.messages.append({"role": "user", "content": transcript})
            with st.chat_message("user"):
                st.write(transcript)

        os.remove(temp_path)

if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)


# Generate assistant reply + audio
# if st.session_state.messages[-1]["role"] != "assistant":
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking 🤔..."):
#             final_response = get_answer(st.session_state.messages)

#         with st.spinner("Generating audio response..."):
#             audio_file = text_to_speech(final_response)
#             autoplay_audio(audio_file)

#         st.write(final_response)
#         st.session_state.messages.append(
#             {"role": "assistant", "content": final_response}
#         )

#         os.remove(audio_file)

if (st.session_state.messages[-1]["role"] != "assistant" and st.session_state.stop_audio == False):
    with st.chat_message("assistant"):
        with st.spinner("Thinking 🤔..."):
            final_response = get_answer(st.session_state.messages)

        with st.spinner("Generating audio response..."):
            audio_file = text_to_speech(final_response)

            # STOP button
            if st.button("Stop Audio"):
                st.session_state.stop_audio = True

            autoplay_audio(audio_file)

        st.write(final_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": final_response}
        )

        os.remove(audio_file)

st.session_state.stop_audio = False


# Stick microphone at bottom
footer_container.float("bottom: 0rem;")
