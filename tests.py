import unittest

from server import app
from model import db, connect_to_db
import re


class ServerTests(unittest.TestCase):
    """Tests for my Vibez site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn(
            b"Vibez", result.data)

    def test_register_page(self):
        result = self.client.get("/register")
        self.assertIn(b"Register an Account!", result.data)
    



class FlaskTests(unittest.TestCase):
    """Flask tests for both valid and invalid login credentials. Use the database and check for flash messages."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app)

        # Create tables and add sample data
        db.create_all()


    # def tearDown(self):
    #     """Do at end of every test."""

    #     db.session.close()
    #     db.drop_all()
    

    def test_login_incorrect_email(self):
        #attempt login with incorrect email credentials
        response = self.client.post('/login', data={
            'email': 'jy.kim@gmail.com',
            'password': 'Elelelel91'
        }, follow_redirects=True)
        self.assertTrue(re.search('No such user',
                        response.get_data(as_text=True)))
    

    
    def test_login_incorrect_password(self):
        #attempt login with incorrect password credentials
        response = self.client.post('/login', data={
            'email': 'jy.kim8295@gmail.com',
            'password': 'Elelelel'
        }, follow_redirects=True)
        self.assertTrue(re.search('Incorrect password',
                                  response.get_data(as_text=True)))

    
    def test_login_correct_user(self):
        #attempt login with correct user credentials
        response = self.client.post('/login', data={
            'email': 'jy.kim8295@gmail.com',
            'password': 'Elelelel91'
        }, follow_redirects=True)
        self.assertTrue(re.search('Logged in.',
                                  response.get_data(as_text=True)))
                                

class FlaskTestsLoggedIn(unittest.TestCase):
    """Flask tests with user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_important_page(self):
        """Test important page."""

        result = self.client.get("/important")
        self.assertIn(b"You are a valued user", result.data)



    
  

if __name__ == "__main__":
    unittest.main()
