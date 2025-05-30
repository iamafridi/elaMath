# if you don't use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()


# Step 1a: Setup Text to Speech – TTS – model with gTTS
import os
from gtts import gTTS

# Step 1b: Setup Text to Speech – TTS – model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs
import platform
import subprocess
from pydub import AudioSegment

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# Step 2: Use Model for Text output to Voice

# Utility function to play audio across different OS
def play_audio(filepath):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', filepath])  # Make sure it's a WAV file
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# Updated gTTS function with MP3 → WAV conversion for compatibility
def text_to_speech_with_gtts(input_text, mp3_path="gtts_testing.mp3", wav_path="gtts_testing.wav"):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(mp3_path)

    # Convert MP3 to WAV using pydub for Linux playback compatibility
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

    play_audio(wav_path)

# Updated ElevenLabs TTS function with MP3 → WAV conversion
def text_to_speech_with_elevenlabs(input_text, mp3_path="elevenlabs_testing.mp3", wav_path="elevenlabs_testing.wav"):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        voice_id="B6PJxMQ0Brihd46NR86u", 
        model_id="eleven_turbo_v2",
        text=input_text
    )
    elevenlabs.save(audio, mp3_path)

    # Convert MP3 to WAV using pydub
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

    play_audio(wav_path)

# Test Input
input_text = "Hi , I am Afridi!"

# Run both TTS functions
print("▶️ Playing gTTS version...")
text_to_speech_with_gtts(input_text)

print("▶️ Playing ElevenLabs version...")
text_to_speech_with_elevenlabs(input_text)



# # if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# #Step1a: Setup Text to Speech–TTS–model with gTTS
# import os
# from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)


# input_text="Hi , I am Afridi"
# # text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# import elevenlabs
# from elevenlabs.client import ElevenLabs
# import os

# ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

# def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio = client.text_to_speech.convert(
#         voice_id="B6PJxMQ0Brihd46NR86u", 
#         model_id="eleven_turbo_v2",
#         text=input_text
#     )
#     elevenlabs.save(audio, output_filepath)

# # text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 


# # *****************************************************************************************************************************************************
#                                               #  You can test this if yours doesnt work ****
# # *****************************************************************************************************************************************************

# # Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# # from elevenlabs.client import ElevenLabs
# # import os

# # ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# # def text_to_speech_with_elevenlabs(input_text, output_filepath):
# #     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
# #     # Use the correct method from the new SDK
# #     audio = client.text_to_speech.convert(
# #         voice_id="B6PJxMQ0Brihd46NR86u",  
# #         model_id="eleven_turbo_v2",
# #         text=input_text
# #     )

# #     with open(output_filepath, "wb") as f:
# #         f.write(audio)

# #     print(f"✅ ElevenLabs audio saved to: {output_filepath}")

# # *************************************************Next Phase *******************

# #Step2: Use Model for Text output to Voice

# import subprocess
# import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi , I am Afridi!"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio = client.text_to_speech.convert(
#         voice_id="B6PJxMQ0Brihd46NR86u", 
#         model_id="eleven_turbo_v2",
#         text=input_text
#     )
#     elevenlabs.save(audio, output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")