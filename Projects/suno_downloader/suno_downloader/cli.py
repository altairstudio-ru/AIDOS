import argparse
from suno_downloader.api_client import APIClient
from suno_downloader.downloader import Downloader
from suno_downloader.storage_manager import StorageManager

def main():
    parser = argparse.ArgumentParser(description='Suno Downloader')
    parser.add_argument('track_id', type=str, help='Track ID to download')
    args = parser.parse_args()

    api_client = APIClient('https://api.suno.com')
    downloader = Downloader(api_client)
    storage_manager = StorageManager('./downloads')

    try:
        audio_data = downloader.download_track(args.track_id, BytesIO())
        output_path = storage_manager.save_track(args.track_id, audio_data.getvalue())
        print(f'Track downloaded and saved to {output_path}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()