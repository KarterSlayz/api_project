import requests
from endpoints.endpoint import Endpoint


class AllMeme(Endpoint):
    def all_meme(self, token):
        self.response = requests.get(
            f'{self.url}/meme',
            headers={'Authorization': token}
        )
        return self.response
