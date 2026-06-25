import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_track(self, track_id):
        response = requests.get(f'{self.base_url}/tracks/{track_id}')
        response.raise_for_status()
        return response.json()