import requests
from endpoints.endpoint import Endpoint
import json
import os
import allure


class Authorize(Endpoint):
    token_file = 'token.json'

    def __init__(self):
        self.token = self.load_token()
        self.response = None

    def load_token(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, 'r') as file:
                return json.load(file).get('token')
        return None

    def save_token(self):
        with open(self.token_file, 'w') as file:
            json.dump({'token': self.token}, file)

    def is_token_valid(self):
        if self.token:
            response = requests.get(f'{self.url}/authorize/{self.token}')
            return response.status_code == 200
        return False

    def authorization(self, name_authorize):
        if not self.is_token_valid():
            self.response = requests.post(f'{self.url}/authorize', json={'name': name_authorize})
            self.token = self.response.json().get('token')
            self.save_token()
        else:
            self.response = requests.Response()
            self.response.status_code = 200
        return self.token

    @allure.step('Check create token.json')
    def check_save_token_json(self):
        with open(self.token_file, 'r') as file:
            assert json.load(file)['token'] == self.token
            print(f'Token save: {json.load(file)['token']}')

    @allure.step('Check valid token')
    def check_valid_token(self):
        response = requests.get(f'{self.url}/authorize/{self.token}')
        assert response.status_code == 200
        print(f'{self.token}', response.text)
