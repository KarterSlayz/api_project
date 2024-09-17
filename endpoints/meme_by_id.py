import requests
from endpoints.endpoint import Endpoint


class MemeById(Endpoint):
    def meme_by_id(self, token, id_meme):
        self.response = requests.get(
            f'{self.url}/meme/{id_meme}',
            headers={'Authorization': token}
        )
        return self.response
