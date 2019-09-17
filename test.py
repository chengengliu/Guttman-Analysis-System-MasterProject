import unittest
from flask_testing import TestCase
from src.views import *


class TestLogin(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_login_success(self):
        response = self.client.post("/auth", data={
            'username': 'test',
            'password': 'test'
        })
        self.assertEqual(response.json, {
            'code': 0,
            'msg': 'Login successful'
        })
        cookie_dict = [cookie for cookie in self.client.cookie_jar]
        self.assertEqual(len(cookie_dict), 1)
        self.assertEqual(cookie_dict[0].name, 'rv_auth')
        self.assertEqual(cookie_dict[0].value, 'e499c0f02e9ed90b4987169a76b920ec3bafb7b6f59e7cc6ffb2b38785696310a6bbe38f5bf81f25108aa859257a85e1')

    def test_login_no_such_user(self):
        response = self.client.post("/auth", data={
            'username': 'test2',
            'password': 'test'
        })
        self.assertEqual(response.json, {
            'code': -1,
            'err_msg': 'User not exist'
        })

    def test_login_wrong_password(self):
        response = self.client.post("/auth", data={
            'username': 'test',
            'password': 'test2'
        })
        self.assertEqual(response.json, {
            'code': -2,
            'err_msg': 'Incorrect password'
        })


if __name__ == '__main__':
    unittest.main()
