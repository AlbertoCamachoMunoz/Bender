from services.services_web_browser import WebBrowserServices as WebBroser
from llama_index import SimpleDirectoryReader
from services.services_openai import OpenAIServices as OpenAi
from graphic_interfaces import GraphicInterfaces
import time
import re


class AppController:
    def __init__(self):
        self.max_token = 1000
        self.web_browser_service = WebBroser()
        self.graphic_interfaces = GraphicInterfaces(self)

    def save_data_from_browser(self, message):
        data = self.web_browser_service.open_browser(message)
        if data is not None:
            self.openai_service = OpenAi(data)
        return data


    def send_chatgpt_question(self, query):
        message = f"[Act step by step] 0 - Please provide Python code wrapped within ```python [code here] ``` (this is the most important part). 1 - Answer the following question: [QUESTION] {query}  "
        result = self.openai_service.make_query(message)
        print(f" Recibiendo mensaje desde open-ai: {result}")
        if result is not None:
            self.write_in_script(result.response)
            return "Racibido"
        else:
            return "Sin respuesta"
    #
    # def write_in_script(self, result):
    #     try:
    #         # Save only the parts of the result that are encapsulated with [```python] CODE [```]
    #         pattern = r"\```python(.*?)\```"
    #         code_parts = re.findall(pattern, result, re.DOTALL)
    #
    #         with open("./responseGPT.py", "w") as file:
    #             for code_part in code_parts:
    #                 file.write(code_part.strip() + "\n")
    #     except Exception as e:
    #         print(f"Error al guardar el archivo script: {e}")

    def write_in_script(self, result):
        try:
            if isinstance(result, str):
                # Save only the parts of the result that are encapsulated with [```python] CODE [```]
                pattern = r"\```python(.*?)\```"
                code_parts = re.findall(pattern, result, re.DOTALL)

                with open("./responseGPT.py", "w") as file:
                    for code_part in code_parts:
                        file.write(code_part.strip() + "\n")
            else:
                print(f"Error: result no es una cadena de caracteres. Tipo de dato: {type(result)}")
        except Exception as e:
            print(f"Error al guardar el archivo script: {e}")