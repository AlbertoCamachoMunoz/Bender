import os
import openai
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


class Singleton(type):
    """
    Singleton metaclass for ensuring only one instance of a class.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    """
    Configuration class to store the state of bools for different scripts access.
    """

    def __init__(self):

        self.fast_llm_model = os.getenv("FAST_LLM_MODEL", "gpt-3.5-turbo")
        self.smart_llm_model = os.getenv("SMART_LLM_MODEL", "gpt-4")
        self.fast_token_limit = int(os.getenv("FAST_TOKEN_LIMIT", 4000))
        self.smart_token_limit = int(os.getenv("SMART_TOKEN_LIMIT", 8000))
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_api_model = os.getenv("OPENAI_API_MODEL")
        self.openai_api_url = os.getenv("OPENAI_API_URL")

        # Initialize the OpenAI API client
        openai.api_key = self.openai_api_key

