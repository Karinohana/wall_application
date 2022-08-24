import os
import unittest
import json
from ..models import db, User
from .base import TestWrapper


class TestUser(TestWrapper):

    

    def test_get_login(self):
        user = User(email="karinohana95@gmail.com", password="12345",
                    first_name="karin", last_name="ohana")
        data = {"email": "karinohana95@gmail.com", "password": "12345"}

        payload = {
            'user': {"email": "karinohana95@gmail.com", "first_name": "karin", "last_name": "ohana", "id": 1},
            "msg": "You've successfully logged in"
        }

        db.session.add(user)
        db.session.commit()

        response = self.app.post('/login', follow_redirects=True, data=json.dumps(
            data), headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["user"], payload["user"])
        self.assertEqual(response.json["msg"], payload["msg"])
        self.assertIn("access_token", response.json.keys())

    def test_get_loginfail(self):
        user = User(email="karinohana95@gmail.com", password="12345",
                    first_name="karin", last_name="ohana")
        data = {"email": "karinohana95@gmail.com", "password": " "}

        payload = {
            'user': {"email": "karinohana95@gmail.com", "first_name": "karin", "last_name": "ohana", "id": 1},
            "msg": "You've successfully logged in"
        }

        db.session.add(user)
        db.session.commit()

        response = self.app.post('/login', follow_redirects=True, data=json.dumps(
            data), headers={'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 401)
        self.assertNotIn("access_token", response.json.keys())