# AIDOS LOG

## Role: coder
## Model: qwen2.5-coder:7b
## Time: 20260624_164619

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
      "content": "import requests\n\nclass APIClient:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        self.base_url = \"https://api.suno.com\""
    },
    {
      "path": "downloader.py",
      "content": "from api_client import APIClient\nimport os\n\nclass Downloader:\n    def __init__(self, client, storage):\n        self.client = client\n        self.storage = storage\n\n    def download_audio(self, audio_id, output_folder):n        response = self.client.get(f'/audio/{audio_id}', headers={'Authorization': f'Bearer {self.client.api_key}'})\n        if response.status_code == 200:\n            file_path = os.path.join(output_folder, f'{audio_id}.mp3')\n            with open(file_path, 'wb') as f:\n                f.write(response.content)\n            return file_path\n        else:\n            raise Exception('Failed to download audio')"
    },
    {
      "path": "storage.py",
      "content": "import os\n\nclass Storage:\n    def __init__(self, base_dir):\n        self.base_dir = base_dir\n\n    def create_folder(self, folder_name):\n        full_path = os.path.join(self.base_dir, folder_name)\n        if not os.path.exists(full_path):\n            os.makedirs(full_path)\n        return full_path"
    },
    {
      "path": "main.py",
      "content": "from downloader import Downloader\nfrom storage import Storage\nimport argparse\n\ndef main():\n    parser = argparse.ArgumentParser(description='Suno Audio Downloader')\n    parser.add_argument('--api_key', type=str, required=True, help='API key for Suno API')\n    parser.add_argument('--audio_id', type=str, required=True, help='ID of the audio to download')\n    parser.add_argument('--output_folder', type=str, default='./downloads', help='Output folder for downloaded audio')\n\n    args = parser.parse_args()\n\n    client = APIClient(args.api_key)\n    storage = Storage(args.output_folder)\n    downloader = Downloader(client, storage)\n\n    output_folder = storage.create_folder('audio')\n    file_path = downloader.download_audio(args.audio_id, output_folder)\n\n    print(f'Audio downloaded to: {file_path}')\n\nif __name__ == '__main__':\n    main()"
    }
  ]
}
```
