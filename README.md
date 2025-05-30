# 🎓 ElaMath – Visual & Vocal Math Assistant
ElaMath is an intelligent, voice-enabled multimodal math assistant designed to help students solve and understand math problems. Simply speak your math question and optionally upload an image—such as a diagram, handwritten notes, or textbook screenshot—and ElaMath will provide clear, step-by-step explanations both in text and spoken audio 

## 📸 Demo

![image](https://github.com/user-attachments/assets/160b2468-8b85-4b0b-951a-1c87b8caf080)


---

## 🧠 AI Models Used

- **Multimodal LLM**: `meta-llama/llama-4-scout-17b-16e-instruct` via **Groq API**
- **Speech Recognition**: **Whisper** (OpenAI)
- **Text-to-Speech**: **gTTS** & **ElevenLabs**

---

## 🛠️ Tech Stack

- ⚡ **Groq API** – High-speed inference for LLaMA models  
- 🧠 **Meta LLaMA-4 Vision Model** – Multimodal math question answering  
- 🎙️ **Whisper** – Converts voice to text  
- 🔊 **gTTS** & **ElevenLabs** – Generate natural audio output  
- 🧪 **Gradio** – Fast web interface for interaction  

---

## 🔍 Key Features

- 🎙️ **Voice Input**: Speak your math question naturally  
- 🖼️ **Image Analysis**: Upload diagrams, equations, or handwritten problems  
- 🧠 **Multimodal Reasoning**: Combines voice + image to give intelligent, relevant answers  
- 💬 **Text + Voice Output**: See and hear the explanation clearly  
- 🌐 **Web Interface**: Lightweight, user-friendly frontend powered by Gradio  

---

## 📁 Project Structure
ElaMath/
├── gradio_app.py                # Main Gradio interface
├── brain_of_the_elaMath.py     # Handles multimodal LLM image + text analysis
├── voice_of_the_user.py        # Speech-to-text logic using Whisper
├── voice_of_the_math_instructor.py # Text-to-speech logic using ElevenLabs/gTTS
├── .env                        # API keys stored securely here


---

## ⚙️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/iamafridi/elaMath.git
cd elaMath

## 2. Add Environment Variables

Create a `.env` file and add the following:

GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

3. Run the Application
python gradio_app.py

### 🧪 Example Use Case  
Upload an image of a geometry problem and ask:

🗣️ “What’s the area of this triangle?”

📢 ElaMath will analyze the image and your voice, then respond with a step-by-step explanation in both text and audio.

---

### 📜 License  
MIT License

---

### 👤 Author  
Afridi Akbar Ifty

GitHub: @iamafridi

Portfolio: iamafrididev.netlify.app

LinkedIn: linkedin.com/in/iamafridi
