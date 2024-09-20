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
        assert self.response.status_code == 400
        print(f'\nTest return status code: {self.response.status_code}')

    @allure.step('Check status code 404')
    def check_status_code_404(self):
        assert self.response.status_code == 404
        print(f'\nTest return status code: {self.response.status_code}')

    @allure.step('Print Error')
    def print_err_test(self):
        print(self.response.text)

    @allure.step('Comparison_of_response_and_stored_data')
    def comparison_of_response_and_stored_data(self, name_authorize):
        with open(self.token_file, 'r') as file:
            assert json.load(file)['token'] and name_authorize in self.response.text
            print(f'Answer {self.response.text} = {self.token} and {name_authorize}')

    @allure.step('Check get mem by id')
    def check_comparison_id(self, id_meme):
        assert str(id_meme) in self.response.text
        print(f'Search mem id: {id_meme} and result searching: {self.response.text}')
