from api_client import APIClient
from downloader import Downloader
from storage import Storage

def main():
    base_url = 'http://example.com/api'
    storage_path = './audio'

    api_client = APIClient(base_url)
    storage = Storage(storage_path)
    downloader = Downloader(storage.get_storage_path())

    track_id = '12345'
    try:
        audio_info = api_client.get_audio(track_id)
        audio_url = audio_info['url']
        file_path = downloader.download_audio(track_id, audio_url)
        print(f'Audio downloaded to: {file_path}')
    except Exception as e:
        print(f'Error: {e.__str__()}')

if __name__ == '__main__':
    main()