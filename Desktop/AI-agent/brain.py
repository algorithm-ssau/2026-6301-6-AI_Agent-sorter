import os
from openai import OpenAI
from dotenv import load_dotenv

class NvidiaBrain:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("NVIDIA_API_KEY")
        self.base_url = os.getenv("NVIDIA_BASE_URL")
        self.model = os.getenv("MODEL_NAME")
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key
        )
    def get_decision(self, system_prompt, user_content):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content