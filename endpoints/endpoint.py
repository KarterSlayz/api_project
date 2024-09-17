import allure
import json
import requests


class Endpoint:
    url = 'http://167.172.172.115:52355'
    token = None
    response = None
    json = None
    token_file = 'token.json'

    @allure.step('Check status code 200')
    def check_status_code_200(self):
        assert self.response.status_code == 200
        print('\nTest return status code 200')

    @allure.step('Check status code 400')
    def check_status_code_400(self):
        if AssertionError:
            print(f'\nTest return status code: {self.response.status_code}')

    @allure.step('Check status code 404')
    def check_status_code_404(self):
        if AssertionError:
            print(f'\nTest return status code: {self.response.status_code}')

    @allure.step('Print Error')
    def print_err_test(self):
        print(self.response.text)

    @allure.step('Comparison_of_response_and_stored_data')
    def comparison_of_response_and_stored_data(self, name_authorize):
        with open(self.token_file, 'r') as file:
            if json.load(file)['token'] and name_authorize in self.response.text:
                print(f'Answer {self.response.text} = {self.token} and {name_authorize}')
            else:
                print('Token and name do not match the answer')

    @allure.step('Check create token.json')
    def check_save_token_json(self):
        with open(self.token_file, 'r') as file:
            print(f'Token save: {json.load(file)['token']}')

    @allure.step('Check valid token')
    def check_valid_token(self):
        response = requests.get(f'{self.url}/authorize/{self.token}')
        print(f'{self.token}', response.text)

    @allure.step('Check get mem by id')
    def check_comparison_id(self, id_meme):
        if str(id_meme) in self.response.text:
            print(f'Search mem id: {id_meme} and result searching: {self.response.text}')

    @allure.step('Check create mem')
    def check_create_mem(self, body):
        common_items = {k: body[k] for k in body if k in self.json and body[k] == self.json[k]}
        if common_items:
            print(f'Mem created with data {body}')
            print(f'Mem: {self.json}')

    @allure.step('Check change mem')
    def check_change_mem(self, body):
        common_items = {k: body[k] for k in body if k in self.json and body[k] == self.json[k]}
        if common_items:
            print(f'Mem changed with data {body}')
            print(f'Mem: {self.json}')
