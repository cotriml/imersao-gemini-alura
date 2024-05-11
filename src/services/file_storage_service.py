import os

class FileStorageService:
    def __init__(self):
      pass

    def get_file_path(self):
      return os.path.join(os.getcwd(), 'files/audio_transcription_sample.txt')