import os
import unittest
import json
from src.api.models import db, User, Posts
from src.test.base import TestWrapper


class TestUser(TestWrapper):

    def test_get_all_posts(self):
        user = User(email="karinohana95@gmail.com", password="12345",
                    first_name="karin", last_name="ohana")
        db.session.add(user)
        db.session.commit()
        posts = Posts(user=User.query.first(), text="test")
        db.session.add(posts)
        db.session.commit()

        response = self.app.get('/posts', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['all_posts']), 1)

    def test_create_post(self):
        user = User(email="karinohana95@gmail.com", password="12345",
                    first_name="karin", last_name="ohana")
        db.session.add(user)
        db.session.commit()

        data = {"email": "karinohana95@gmail.com", "password": "12345"}
        login = self.app.post('/login', follow_redirects=True,
                              data=json.dumps(data), headers={'Content-Type': 'application/json'})
        create_post_data = {"text": "test"}
        headers = {'Content-Type': 'application/json',
                   "Authorization": f"Bearer {login.json['access_token']}"}
        create_post = self.app.post(
            '/create_post', follow_redirects=True, data=json.dumps(create_post_data), headers=headers)
        self.assertEqual(create_post.status_code, 200)
        self.assertEqual(create_post.json["post"]["text"], "test")

        response = self.app.get('/posts', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['all_posts']), 1)