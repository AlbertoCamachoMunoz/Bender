import openai
import requests
import json
from ChatGPTWebScrapping.config import Config

cfg = Config()
# Load credentials for OpenAI API authentication
import os
import openai
openai.api_key = cfg.openai_api_url
audio_file = open("./audio/x.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)
