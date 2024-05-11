import google_generativeai as genai
import os

class GoogleGeminiServices:
    def __init__(self):
      self.GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
      self.configure_genai()

    def configure_genai(self):
      try:
        genai.configure(api_key=self.GEMINI_API_KEY)
      except Exception as e:
        print(f"Error configuring GenAI: {e}")

    def instance_model(self):
      gen_config = {
        "candidate_count": 1,
        "temperature": 0.9
      }
      try:
        model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=gen_config)
      except Exception as e:
        print(f"Error instantiating GenAI model: {e}")
      
      return model




