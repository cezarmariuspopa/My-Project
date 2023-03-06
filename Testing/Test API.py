from requests_api.api_clients import *

class TestApiClient:
    nr = randint(1, 9999999)
    clientName = 'CezarTest'
    clientEmail = f'email_test{nr}@xmail.com'

    def setup_method(self):
        self.response = login(self.clientName, self.clientEmail)

    def test_succesful_login(self):
        assert self.response.status_code == 201, 'Actual status code is not correct'
        assert 'accessToken' in self.response.json().keys(), 'Token property is not present in the response'

    def test_login_already_registered(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409, 'Actual status code is not correct'
        assert self.response.json()['error'] == 'API client already registered. Try a different email.'

    def test_invalid_email(self):
        self.response = login('def', 'abc')
        assert self.response.status_code == 400, 'Actual status code is not correct'
        assert self.response.json()['error'] == 'Invalid or missing client email.'