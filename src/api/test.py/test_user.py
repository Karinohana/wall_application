import os
import unittest
import json
from ..models import db, User
from .base import TestWrapper


class TestUser(TestWrapper):


    def test_get_all_users(self):
        user = User(email="karinohana95@gmail.com", password="12345",
                    first_name="karin", last_name="ohana")
        data = {"email": "the.wall.application.test@gmail.com",
                "password": "12345", "first_name": "test", "last_name": "test"}
        db.session.add(user)
        db.session.commit()

        response = self.app.post('/register', follow_redirects=True, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['user']), 1)