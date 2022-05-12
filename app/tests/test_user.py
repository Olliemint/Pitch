import unittest
from app.models import User,Pitch

class TestUsers(unittest.TestCase):
    """
    This is the class which we will use to do tests for the User
    """
    def setUp(self):
        """
        This will create an instance of the User before each test case
        """

        self.new_user = User(name = "Ollie", password = "test")

    def tearDown(self):
        """
        Will delete all the info from the db
        """
        User.query.delete()
        Pitch.query.delete()

    def test_instance(self):
        """
        Will test whether the new instance is an instance of the User model
        """
        self.assertTrue(isinstance(self.new_user, User))

    def test_init(self):
        """
        Will test whether the User model is instantiated correctly
        """
        self.assertEqual(self.new_user.name,"Ollie")

    def test_password_generate(self):
        """
        Will test whether a password is generated
        """
        self.assertTrue(self.new_user.pass_locked is not None)
    
    def test_password_is_hashed(self):
        """
        Will test whether the password generated is not equal to the inputted password
        """
        self.assertTrue(self.new_user.pass_locked is not "test")

    def test_password_verifier(self):
        """
        Will test whether the user can decrypt the password with their password
        """
        self.assertTrue(self.new_user.verify_password("test"))

    def test_save_user(self):
        """
        Will test whether the user is saved into the database
        """
        self.new_user.save_user()
        users = User.query.all()
        self.assertTrue(len(users) > 0)