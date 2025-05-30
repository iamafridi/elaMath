import os
import base64
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Function to encode image as base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to analyze image with a query
def analysis_image_with_query(query, encoded_image, model="meta-llama/llama-4-maverick-17b-128e-instruct"):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return chat_completion.choices[0].message.content


