import os
import unittest
import json
from src.api.models import db, User
from src.test.base import TestWrapper


class TestUser(TestWrapper):


    def test_register(self):
        data = {"email": "the.wall.application.test@gmail.com",
                "password": "12345", "first_name": "test", "last_name": "test"}
        

        response = self.app.post('/register', follow_redirects=True, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        user = User.query.filter_by(email = data["email"]).all()
        self.assertEqual(len(user),1)
        self.assertEqual(user[0].email,data["email"])
        self.assertEqual(user[0].password,data["password"])
        self.assertEqual(user[0].first_name,data["first_name"])
        self.assertEqual(user[0].last_name,data["last_name"])