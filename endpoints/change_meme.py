import allure
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

    @allure.step('Check change mem')
    def check_change_mem(self, body):
        common_items = {k: body[k] for k in body if k in self.json and body[k] == self.json[k]}
        assert common_items
        print(f'Mem changed with data {body}')
        print(f'Mem: {self.json}')
