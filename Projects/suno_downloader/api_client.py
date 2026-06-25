import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_audio(self, track_id):
        response = requests.get(f'{self.base_url}/track/{track_id}')
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Failed to fetch audio')