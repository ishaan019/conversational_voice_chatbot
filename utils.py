# import streamlit as st
# from openai import OpenAI

# load_dotenv()

# api_key = os.getenv("openai_api_key")

# client = OpenAI(api_key=api_key)

# def speech_to_text(audio_data):
#     with open(audio_data, "rb") as audio_file:
#         transcript = client.audio.transcriptions.create(
#             model="whisper-1",
#             response_format="text",
#             file=audio_file
#         )
#     return transcript

# def text_to_speech(input_text):
#     response = client.audio.speech.create(
#         model="tts-1",
#         voice="nova",
#         input=input_text
#     )
#     webm_file_path = "temp_audio_play.mp3"
#     with open(webm_file_path, "wb") as f:
#         response.stream_to_file(webm_file_path)
#     return webm_file_path

# def get_answer(messages):
#     system_message = [{"role": "system", "content": "You are an helpful AI chatbot, that answers questions asked by User."}]
#     messages = system_message + messages
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo-1106",
#         messages=messages
#     )
#     return response.choices[0].message.content

# def autoplay_audio(file_path):
#     """Autoplay audio in Streamlit."""
#     with open(file_path, "rb") as f:
#         data = f.read()
#     b64 = base64.b64encode(data).decode("utf-8")
#     md=f"""
#     <audio autoplay>
#     <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#     </audio>
#     """
#     st.markdown(md, unsafe_allow_html=True)


import os
import base64
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# api_key = os.getenv("openai_api_key")
api_key = "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"

client = OpenAI(api_key=api_key)


def speech_to_text(audio_data):
    with open(audio_data, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file
        )
    return transcript


def text_to_speech(input_text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=input_text
    )
    file_path = "temp_audio_play.mp3"
    with open(file_path, "wb") as f:
        response.stream_to_file(file_path)
    return file_path


# def get_answer(messages):
#     system_message = [
#         {
#             "role": "system",
#             "content": "You are a helpful AI chatbot that answers questions asked by the user."
#         }
#     ]
#     messages = system_message + messages

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo-1106",
#         messages=messages
#     )
#     return response.choices[0].message.content

def get_answer(messages):
    system_message = [
        {
            "role": "system",
            "content": "You are a helpful AI chatbot that answers questions asked by the user."
        }
    ]
    messages = system_message + messages

    response = client.chat.completions.create(
        model="gpt-5-nano-2025-08-07",
        messages=messages
    )
    return response.choices[0].message.content


def autoplay_audio(file_path):
    """Inject auto-play audio using HTML."""
    with open(file_path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode("utf-8")

    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(audio_html, unsafe_allow_html=True)
