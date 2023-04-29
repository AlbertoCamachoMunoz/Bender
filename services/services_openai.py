import requests
import json
from ChatGPTWebScrapping.config import Config

cfg = Config()
class OpenAIServices:
    def __init__(self):
        self.OPENAI_API_KEY = cfg.openai_api_key
        self.URL = cfg.openai_api_url
        self.model = cfg.openai_api_model

    def make_request(self, message):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.OPENAI_API_KEY}",
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": message}],
            "temperature": 0.7,
        }

        response = requests.post(self.URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            result = response.json()
            return self.extract_content(result)
        else:
            print(f"Error al conectarse a la API: {response.status_code}")
            return None

    def extract_content(self, api_response):
        content = api_response['choices'][0]['message']['content']
        return content

