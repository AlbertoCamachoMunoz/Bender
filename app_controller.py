from services.services_web_browser import WebBrowserServices as WebBroser
from services.services_openai import OpenAIServices as OpenAi
from graphic_interfaces import GraphicInterfaces

class AppController:
    def __init__(self):
        self.max_token = 2000
        self.openai_service = OpenAi()
        self.web_browser_service = WebBroser()
        self.graphic_interfaces = GraphicInterfaces(self)

    def find_in_browser(self, message):
        result = self.web_browser_service.open_browser(message)
        print(f" Recibiendo mensaje desde web_broser: {result}")
        return result

    def send_chatgpt_question(self, question, page_content):
        # Lógica para enviar la pregunta a ChatGPT

        # recorrer cada 2000
        if page_content:
            total_segments = len(page_content) // self.max_token + 1
            for i in range(0, len(page_content), self.max_token):
                if(i > 20): break
                is_last_iteration = (i // self.max_token) == (total_segments - 1)
                segment = page_content[i:i + self.max_token]
                message = f"Context: {segment}\n"
                result = self.openai_service.make_request(message)

            message = f"Question for the last Context: {question}"
            print(f" Recibiendo mensaje desde open-ai: {message}")
            return self.openai_service.make_request(message)

