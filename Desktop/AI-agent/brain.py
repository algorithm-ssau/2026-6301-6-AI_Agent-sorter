import os
from openai import OpenAI
from dotenv import load_dotenv

class NvidiaBrain:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("NVIDIA_API_KEY")
        self.base_url = os.getenv("NVIDIA_BASE_URL")
        self.model = os.getenv("MODEL_NAME")