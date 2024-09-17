import requests
from endpoints.endpoint import Endpoint


class ChangeMeme(Endpoint):
    def change_meme(self, meme_id, token, body):
        body = {"id": meme_id, **body}
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=body,
            headers={'Authorization': token}
        )
        self.json = self.response.json()
        return self.json
