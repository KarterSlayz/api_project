import requests
from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    def delete_meme(self, meme_id, token):
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            headers={'Authorization': token}
        )
        print(self.response.status_code)
        return self.response
