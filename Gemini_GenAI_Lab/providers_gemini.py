import os
from google import genai

class GeminiProvider:
    def __init__(self):
        key=os.getenv("GEMINI_API_KEY")
        model=os.getenv("GEMINI_MODEL")
        if not key: raise RuntimeError("GEMINI_API_KEY is missing in .env")
        if not model: raise RuntimeError("GEMINI_MODEL is missing in .env")
        self.client=genai.Client(api_key=key)
        self.model=model

    def generate(self,prompt):
        response=self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text
