import requests
from io import BytesIO
import os

class Downloader:
    def __init__(self, api_client):
        self.api_client = api_client

    def download_track(self, track_id, output_path):
        track_data = self.api_client.get_track(track_id)
        audio_url = track_data['audio_url']

        response = requests.get(audio_url, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)