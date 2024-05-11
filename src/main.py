from usecases import ai_model_generate_content, read_audio_transcription_file, get_prompt

def main():
  file_content = read_audio_transcription_file.read_file()
  
  prompt = "Com a transcrição de um audio de uma entrevista de emprego, gere em formato de perguntas e respostas o que foi conversado nessa entrevista, no final dê um feedback de sentimento de como o entrevistado foi. Traduza para portugês." + file_content

  generated_content = ai_model_generate_content.generate_content(prompt)
  print(generated_content)

if __name__ == "__main__":
  main()