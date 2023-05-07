from ChatGPTWebScrapping.config import Config
import openai
import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, Document,  LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI

cfg = Config()
class OpenAIServices:
    def __init__(self, data):
        pdf = '../data/data.pdf'
        self.OPENAI_API_KEY = cfg.openai_api_key
        self.URL = cfg.openai_api_url
        # self.pdf = SimpleDirectoryReader('../data/data.pdf').load_data()
        # self.model = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name=cfg.openai_api_model))
        self.model = LLMPredictor(llm=ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo'))
        self.service_context = ServiceContext.from_defaults(llm_predictor=self.model)
        # self.index = GPTVectorStoreIndex.from_documents(self.pdf, service_context=self.service_context)
        # Por estas nuevas líneas:
        doc = Document(data)
        self.index = GPTVectorStoreIndex.from_documents([doc], service_context=self.service_context, disallowed_special=())

    def make_query(self, query):
        try:
            content = self.index.as_query_engine().query(query)
        except Exception as e:
            print(f"Error al guardar el archivo HTML: {e}")
            content = e
        return content

