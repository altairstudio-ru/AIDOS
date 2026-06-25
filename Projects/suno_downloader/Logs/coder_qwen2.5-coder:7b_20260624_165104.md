# AIDOS LOG

## Role: coder
## Model: qwen2.5-coder:7b
## Time: 20260624_165104

---

## INPUT
Suno Downloader

---

## OUTPUT
{
  "files": [
    {
      "path": "suno_downloader/api_client.py",
      "content": "import requests\n\nclass APIClient:\n    def __init__(self, base_url):\n        self.base_url = base_url\n\n    def get_track(self, track_id):\n        response = requests.get(f'{self.base_url}/tracks/{track_id}')\n        response.raise_for_status()\n        return response.json()"
    },
    {
      "path": "suno_downloader/downloader.py",
      "content": "import requests\nfrom io import BytesIO\nimport os\n\nclass Downloader:\n    def __init__(self, api_client):\n        self.api_client = api_client\n\n    def download_track(self, track_id, output_path):\n        track_data = self.api_client.get_track(track_id)\n        audio_url = track_data['audio_url']\n\n        response = requests.get(audio_url, stream=True)\n        response.raise_for_status()\n\n        with open(output_path, 'wb') as f:\n            for chunk in response.iter_content(chunk_size=8192):\n                if chunk:\n                    f.write(chunk)"
    },
    {
      "path": "suno_downloader/storage_manager.py",
      "content": "import os\n\nclass StorageManager:\n    def __init__(self, base_path):\n        self.base_path = base_path\n\n    def save_track(self, track_id, audio_data):\n        output_path = os.path.join(self.base_path, f'{track_id}.mp3')\n        with open(output_path, 'wb') as f:\n            f.write(audio_data)\n        return output_path"
    },
    {
      "path": "suno_downloader/cli.py",
      "content": "import argparse\nfrom suno_downloader.api_client import APIClient\nfrom suno_downloader.downloader import Downloader\nfrom suno_downloader.storage_manager import StorageManager\n\ndef main():\n    parser = argparse.ArgumentParser(description='Suno Downloader')\n    parser.add_argument('track_id', type=str, help='Track ID to download')\n    args = parser.parse_args()\n\n    api_client = APIClient('https://api.suno.com')\n    downloader = Downloader(api_client)\n    storage_manager = StorageManager('./downloads')\n\n    try:\n        audio_data = downloader.download_track(args.track_id, BytesIO())\n        output_path = storage_manager.save_track(args.track_id, audio_data.getvalue())\n        print(f'Track downloaded and saved to {output_path}')\n    except Exception as e:\n        print(f'Error: {e}')\n\nif __name__ == '__main__':\n    main()"
    }
  ]
}
