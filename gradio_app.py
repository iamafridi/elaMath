
# **************************************************************************************************************************
# Please run this first : pipenv install groq dotenv gtts elevenlabs dotenv pydub gradio SpeechRecognition
# **************************************************************************************************************************


# # UI with gradio
import os
import gradio as gr

from brain_of_the_elaRech import encode_image, analysis_image_with_query  # keep your original function name
from voice_of_the_user import record_audio, transcribe_with_groq
from voice_of_the_math_instructor import play_audio, text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt = """You have to act as a professional math_instructor (this is for learning purposes). 
What's in this image? Do you find anything notable or significant about it scientifically? 
If you can make any observations or hypotheses, suggest possible explanations or next steps. 
Do not add any numbers or special characters in your response. 
Your response should be one long paragraph. 
Always answer as if you are speaking to a real person. 
Do not say 'In the image I see'; instead, say 'With what I observe, I think...'. 
Do not respond as an AI model or use markdown. 
Your answer should mimic that of an actual math_instructor, not an AI bot. 
Keep your answer concise (max 2 sentences). 
No preamble; start your answer right away, please."""

def process_inputs(audio_filepath, image_filepath):
    # Audio theke text ber korchi, pore image analyze korbo
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    if image_filepath:
        researcher_response = analysis_image_with_query(
            query=system_prompt + " " + speech_to_text_output, 
            encoded_image=encode_image(image_filepath), 
            model="meta-llama/llama-4-maverick-17b-128e-instruct"
        )
    else:
        researcher_response = "No image provided for me to analyze"

    # ElevenLabs diye speech banacchi, file path fixed to 'final.wav' for compatibility with play_audio
    voice_output_path = "final.wav"
    text_to_speech_with_elevenlabs(input_text=researcher_response, mp3_path="final.mp3", wav_path=voice_output_path)
    
    # Return text from audio, researcher response, and audio file path for Gradio audio output
    return speech_to_text_output, researcher_response, voice_output_path

iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        # gr.Textbox(label="Speech to Text"),
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        # gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="ElaMath's Response"),
        gr.Audio(label="Voice Response")
    ],
    title="AI ElaMath with Vision and Voice - Deepseek-r1-distill-llama-70b Model"
)

iface.launch(debug=True)



# Host : http://127.0.0.1:7860



# *******************************************
#             Prev one 
# **************************************
# import os
# import gradio as gr

# from brain_of_the_elaRech import encode_image,analysis_image_with_query
# from voice_of_the_user import record_audio,transcribe_with_groq
# from voice_of_the_researcher import play_audio,text_to_speech_with_gtts,text_to_speech_with_elevenlabs

# system_prompt = """You have to act as a professional researcher (this is for learning purposes). 
# What's in this image? Do you find anything notable or significant about it scientifically? 
# If you can make any observations or hypotheses, suggest possible explanations or next steps. 
# Do not add any numbers or special characters in your response. 
# Your response should be one long paragraph. 
# Always answer as if you are speaking to a real person. 
# Do not say 'In the image I see'; instead, say 'With what I observe, I think...'. 
# Do not respond as an AI model or use markdown. 
# Your answer should mimic that of an actual researcher, not an AI bot. 
# Keep your answer concise (max 2 sentences). 
# No preamble; start your answer right away, please."""



# def process_inputs(audio_filepath, image_filepath):
#     speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
#                                                  audio_filepath=audio_filepath,
#                                                  stt_model="whisper-large-v3")

#     # Handle the image input
#     if image_filepath:
#         researcher_response = analysis_image_with_query(query=system_prompt+speech_to_text_output, encoded_image=encode_image(image_filepath), model="meta-llama/llama-4-maverick-17b-128e-instruct")
#     else:
#         researcher_response = "No image provided for me to analyze"

#     voice_of_researcher = text_to_speech_with_elevenlabs(input_text=researcher_response, output_filepath="final.mp3") 

#     return speech_to_text_output, researcher_response, voice_of_researcher


# # Create the interface
# iface = gr.Interface(
#     fn=process_inputs,
#     inputs=[
#         gr.Audio(sources=["microphone"], type="filepath"),
#         gr.Image(type="filepath")
#     ],
#     outputs=[
#         gr.Textbox(label="Speech to Text"),
#         gr.Textbox(label="ElaRech's Response"),
#         gr.Audio("Temp.mp3")
#     ],
#     title="AI ElaRech with Vision and Voice"
# )

# iface.launch(debug=True)