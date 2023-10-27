import unittest
from unittest.mock import patch
from server import create_app

class TestUnitServerMethods(unittest.TestCase):

    def setUp(self):
        self.app_instance = create_app()
        self.app_instance.config['TESTING'] = True
        self.app = self.app_instance.test_client()

    @patch('server.loadClubs')
    def test_loadClubs(self, mock_loadClubs):
        mock_clubs = [{'name': 'Club A'}, {'name': 'Club B'}]
        mock_loadClubs.return_value = mock_clubs

    @patch('server.loadCompetitions')
    def test_loadCompetitions(self, mock_loadCompetitions):
        mock_competitions = [{'name': 'Competition A'}, {'name': 'Competition B'}]
        mock_loadCompetitions.return_value = mock_competitions

    def test_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(response.location.endswith('/'))

if __name__ == '__main__':
    unittest.main()
