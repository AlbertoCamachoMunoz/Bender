
import openai
import requests

openai.api_key = "YOUR-API-KEY"

url = "https://api.openai.com/v1/audio/translations"

file_path = "./audio/x.wav"
model_id = "whisper-1"

headers = {
    "Authorization": f"Bearer {openai.api_key}",
}

data = {
    "model": (None, "whisper-1"),
    "file": ("x.wav", open("./audio/x.wav", "rb")),
}

response = requests.post(url, headers=headers, files=data)

# transcription = response.json()["text"]
print(response.content)