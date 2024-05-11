from services import google_gemini_services

google_gemini_services = google_gemini_services.GoogleGeminiServices()

def generate_content(prompt: str):
  model = google_gemini_services.instance_model()
  response = model.generate_content(prompt)
  return response
