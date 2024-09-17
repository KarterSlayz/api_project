import requests
from endpoints.endpoint import Endpoint


class AddMeme(Endpoint):
    meme_id = None

    def add_meme(self, token, body):
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers={'Authorization': token}
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.meme_id = self.json['id']
        return self.json
