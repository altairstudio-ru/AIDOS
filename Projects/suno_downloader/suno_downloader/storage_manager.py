import os

class StorageManager:
    def __init__(self, base_path):
        self.base_path = base_path

    def save_track(self, track_id, audio_data):
        output_path = os.path.join(self.base_path, f'{track_id}.mp3')
        with open(output_path, 'wb') as f:
            f.write(audio_data)
        return output_path