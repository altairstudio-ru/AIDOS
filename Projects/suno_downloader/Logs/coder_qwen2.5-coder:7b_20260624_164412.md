# AIDOS LOG

## Role: coder
## Model: qwen2.5-coder:7b
## Time: 20260624_164412

---

## INPUT
Suno Downloader

---

## OUTPUT
```json
{
  "files": [
    {
      "path": "api_client.py",
      "content": """
import requests

class SunoAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.suno.com'

    def get_audio_data(self, audio_id):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(f'{self.base_url}/audio/{audio_id}', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to retrieve audio data')
      """
    },
    {
      "path": "downloader.py",
      "content": """
import os
from api_client import SunoAPIClient

class AudioDownloader:
    def __init__(self, api_key):
        self.api_client = SunoAPIClient(api_key)

    def download_audio(self, audio_id, output_dir):
        audio_data = self.api_client.get_audio_data(audio_id)
        file_name = f"{audio_data['title']}.mp3"
        output_path = os.path.join(output_dir, file_name)
        
        with open(output_path, 'wb') as f:
            f.write(audio_data['data'])
        
        return output_path
      """
    },
    {
      "path": "storage.py",
      "content": """
import shutil
from datetime import datetime

class FileManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

    def organize_files(self, files):
        for file in files:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            new_path = os.path.join(self.base_dir, f"{timestamp}_{os.path.basename(file)}")
            shutil.move(file, new_path)
      """
    },
    {
      "path": "main.py",
      "content": """
import argparse
from downloader import AudioDownloader
from storage import FileManager

def main():
    parser = argparse.ArgumentParser(description='Suno Downloader')
    parser.add_argument('--api-key', required=True, help='API key for Suno API')
    parser.add_argument('--audio-id', required=True, help='Audio ID to download')
    parser.add_argument('--output-dir', default='./downloads', help='Output directory for downloaded files')

    args = parser.parse_args()

    downloader = AudioDownloader(args.api_key)
    audio_path = downloader.download_audio(args.audio_id, args.output_dir)

    file_manager = FileManager(args.output_dir)
    file_manager.organize_files([audio_path])

if __name__ == '__main__':
    main()
      """
    }
  ]
}
```
