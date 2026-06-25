import os
from urllib.request import urlretrieve

class Downloader:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def download_audio(self, track_id, audio_url):
        file_name = f'{track_id}.mp3'
        full_path = os.path.join(self.storage_path, file_name)
        urlretrieve(audio_url, full_path)
        return full_path