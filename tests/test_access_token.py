import unittest
from app import create_app
from app.utils.platform import get_access_token 
class TestAccessToken(unittest.TestCase):
    def test_access_token(self):
        access_token = get_access_token()
        self.assertNotEquals(access_token,None)


if __name__ == "__main__":
    unittest.main(verbosity=2)