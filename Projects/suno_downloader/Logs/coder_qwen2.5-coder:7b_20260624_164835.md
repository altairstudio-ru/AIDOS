# AIDOS LOG

## Role: coder
## Model: qwen2.5-coder:7b
## Time: 20260624_164835

---

## INPUT
Suno Downloader

---

## OUTPUT
{
  "files": [
    {
      "path": "api_client.py",
      "content": "import requests\n\nclass APIClient:\n    def __init__(self, base_url):\n        self.base_url = base_url\n\n    def get_audio(self, track_id):\n        response = requests.get(f'{self.base_url}/track/{track_id}')\n        if response.status_code == 200:\n            return response.json()\n        else:\n            raise Exception('Failed to fetch audio')"
    },
    {
      "path": "downloader.py",
      "content": "import os\nfrom urllib.request import urlretrieve\n\nclass Downloader:\n    def __init__(self, storage_path):\n        self.storage_path = storage_path\n\n    def download_audio(self, track_id, audio_url):\n        file_name = f'{track_id}.mp3'\n        full_path = os.path.join(self.storage_path, file_name)\n        urlretrieve(audio_url, full_path)\n        return full_path"
    },
    {
      "path": "storage.py",
      "content": "import os\n\nclass Storage:\n    def __init__(self, base_path):\n        self.base_path = base_path\n        if not os.path.exists(self.base_path):\n            os.makedirs(self.base_path)\n\n    def get_storage_path(self):\n        return self.base_path"
    },
    {
      "path": "main.py",
      "content": "from api_client import APIClient\nfrom downloader import Downloader\nfrom storage import Storage\n\ndef main():\n    base_url = 'http://example.com/api'\n    storage_path = './audio'\n\n    api_client = APIClient(base_url)\n    storage = Storage(storage_path)\n    downloader = Downloader(storage.get_storage_path())\n\n    track_id = '12345'\n    try:\n        audio_info = api_client.get_audio(track_id)\n        audio_url = audio_info['url']\n        file_path = downloader.download_audio(track_id, audio_url)\n        print(f'Audio downloaded to: {file_path}')\n    except Exception as e:\n        print(f'Error: {e.__str__()}')\n\nif __name__ == '__main__':\n    main()"
    }
  ]
}
