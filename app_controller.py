from services.services_web_browser import WebBrowserServices as WebBroser
from services.services_openai import OpenAIServices as OpenAi
from graphic_interfaces import GraphicInterfaces
import time
import re


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
        if page_content:
            # Dividiendo el contenido de la página en bloques de 2000 palabras
            words = page_content.split()
            segments = [' '.join(words[i:i + self.max_token]) for i in range(0, len(words), self.max_token)]

            for i, segment in enumerate(segments):
                # if i in (2,3):
                message = f"[Act in a minimalistic manner, respond with the least amount of characters, as it is the most important] Context {i}: {segment}\n"
                print(f" fragmento {i}  {message}")
                result = self.openai_service.make_request(message)
                print(f" result {i}  {result}")
                time.sleep(15)

            message = f"[Act step by step] 0- you only response code python , is the most important 1- Join each previus context and resolve my question: {question}"
            print(f" Enviendo mensaje desde open-ai: {message}")
            result = self.openai_service.make_request(message)
            print(f" Recibiendo mensaje desde open-ai: {result}")
            self.write_in_script(result)

            return result

    def write_in_script(self, result):
        # Save only the parts of the result that are encapsulated with [```python] CODE [```]
        pattern = r"\```python(.*?)\```"
        code_parts = re.findall(pattern, result, re.DOTALL)

        with open("./responseGPT.py", "w") as file:
            for code_part in code_parts:
                file.write(code_part.strip() + "\n")