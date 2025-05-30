
# **************************************************************************************************************************
# Please run this first : pipenv install groq dotenv gtts elevenlabs dotenv pydub gradio SpeechRecognition
# **************************************************************************************************************************
import os
import gradio as gr

from brain_of_the_elaMath import encode_image, analysis_image_with_query
from voice_of_the_user import transcribe_with_groq
from voice_of_the_math_instructor import text_to_speech_with_elevenlabs

# Updated Prompt for a Math Assistant
system_prompt = """You are a helpful, knowledgeable math assistant AI who helps users solve math questions of all types—algebra, geometry, calculus, number theory, and more. 
Answer clearly, concisely, and in simple language that suits the user level (beginner, intermediate, or advanced).
Always provide reasoning for the steps if relevant. 
Only focus on the math question and the image provided. Avoid small talk or AI disclaimers.
No markdown formatting or special characters—just plain explanations.
Avoid saying things like “As an AI...” or “In the image, I see...”.
Start directly with your math explanation."""

def process_inputs(audio_filepath, image_filepath, progress=gr.Progress(track_tqdm=True)):
    progress(0.1, desc="Transcribing audio...")

    try:
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
    except Exception as e:
        speech_to_text_output = "There was a problem transcribing your audio."

    if not isinstance(speech_to_text_output, str) or not speech_to_text_output.strip():
        speech_to_text_output = "No question was captured from the audio."

    progress(0.5, desc="Analyzing image...")

    if image_filepath:
        try:
            researcher_response = analysis_image_with_query(
                query=f"{system_prompt}\n\nQuestion: {speech_to_text_output}",        
                encoded_image=encode_image(image_filepath),
                model="meta-llama/llama-4-maverick-17b-128e-instruct"
            )
        except Exception as e:
            researcher_response = f"Failed to analyze image. Error: {str(e)}"
    else:
        researcher_response = "No image provided for me to analyze."

    progress(0.8, desc="Generating voice response...")

    voice_output_path = "final.wav"
    text_to_speech_with_elevenlabs(
        input_text=researcher_response, 
        mp3_path="final.mp3", 
        wav_path=voice_output_path
    )

    progress(1.0, desc="Done!")

    return speech_to_text_output, researcher_response, voice_output_path


with gr.Blocks(css="""
body {
    background: black;
}
#main-title {
    text-align: center;
    font-weight: extra-bold;
    font-size: 3.8em;
    background: linear-gradient(90deg, #00796b, #004d40);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: uppercase;
}
#footer {
    text-align: center;
    margin-top: 2em;
    color: #004d40;
    font-weight: bold;
}
""") as demo:

    gr.Markdown("## ElaMath -- Visual & Vocal Math Assistant", elem_id="main-title")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🎤 Input")
            audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Speak your math question")
            image_input = gr.Image(type="filepath", label="Upload a scientific/math image")

        with gr.Column(scale=1):
            gr.Markdown("### 📢 Output")
            text_output = gr.Textbox(label="📝 Speech to Text Result")
            ai_response = gr.Textbox(label="📚 ElaMath's Explanation")
            voice_output = gr.Audio(label="🔊 Listen to the Explanation")

    submit_btn = gr.Button("🚀 Analyze & Speak")

    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[text_output, ai_response, voice_output]
    )

    gr.Markdown("Created by Afridi Akbar Ifty", elem_id="footer")

demo.launch(debug=True)




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