import requests
import allure
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

    @allure.step('Check create mem')
    def check_create_mem(self, body):
        common_items = {k: body[k] for k in body if k in self.json and body[k] == self.json[k]}
        assert common_items
        print(f'Mem created with data {body}')
        print(f'Mem: {self.json}')