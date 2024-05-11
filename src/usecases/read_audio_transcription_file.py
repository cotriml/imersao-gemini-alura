from services import file_storage_service

file_storage_service = file_storage_service.FileStorageService()

def read_file():
  file_path = file_storage_service.get_file_path()
  audio_transcription_text = ""
  with open(file_path) as f:
      audio_transcription_text = f.read()

  return audio_transcription_text