import unittest
from unittest.mock import patch
from server import create_app

class TestFunctionalServerMethods(unittest.TestCase):

    def setUp(self):
        self.app_instance = create_app()
        self.app_instance.config['TESTING'] = True
        self.app = self.app_instance.test_client()

    @patch('server.loadClubs')
    @patch('server.loadCompetitions')
    @patch('server.saveClubs')
    @patch('server.saveCompetitions')
    def test_showSummary_valid_email(self, mock_saveCompetitions, mock_saveClubs, mock_loadCompetitions, mock_loadClubs):
        mock_loadClubs.return_value = [{"name": "Simply Lift", "email": "john@simplylift.com", "points": "10"}]
        mock_loadCompetitions.return_value = [{"name": "Spring Festival", "date": "2024-03-27 10:00:00", "numberOfPlaces": "9"}]
        response = self.app.post('/showSummary', data={'email': 'john@simplylift.com'})
        self.assertIn(b'Welcome, john@simplylift.com', response.data)

    def test_showSummary_invalid_email(self):
        response = self.app.post('/showSummary', data={'email': 'invalid@invalid.com'})
        self.assertEqual(response.status_code, 302)

    def test_book_competition_valid(self):
        response = self.app.get('/book/Spring Festival/Simply Lift')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Booking for Spring Festival', response.data)

    @patch('server.loadClubs')
    @patch('server.loadCompetitions')
    @patch('server.saveClubs')
    @patch('server.saveCompetitions')
    def test_purchase_places_valid(self, mock_saveCompetitions, mock_saveClubs, mock_loadCompetitions, mock_loadClubs):
        mock_loadClubs.return_value = [{"name": "Simply Lift", "email": "john@simplylift.com", "points": "10"}]
        mock_loadCompetitions.return_value = [{"name": "Spring Festival", "date": "2024-03-27 10:00:00", "numberOfPlaces": "9"}]
        response = self.app.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '3'})
        self.assertIn(b'Great-booking complete!', response.data)

    def test_book_with_insufficient_points(self):
        with patch('server.loadClubs') as mock_loadClubs, patch('server.loadCompetitions') as mock_loadCompetitions:
            mock_loadClubs.return_value = [{"name": "Simply Lift", "email": "john@simplylift.com", "points": "1"}]
            mock_loadCompetitions.return_value = [{"name": "Spring Festival", "date": "2024-03-27 10:00:00", "numberOfPlaces": "9"}]
            response = self.app.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '3'})
            self.assertIn(b'Not enough points to complete this booking', response.data)

    def test_purchase_more_places_than_available(self):
        response = self.app.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '20'})
        self.assertIn(b'Not enough points to complete this booking', response.data)

    @patch('server.loadClubs', return_value=[{'name': 'Club A'}, {'name': 'Club B'}])
    @patch('server.loadCompetitions', return_value=[{'name': 'Competition A'}, {'name': 'Competition B'}])
    @patch('server.saveClubs')
    @patch('server.saveCompetitions')
    def test_book_competition_invalid_club_or_competition(self, mock_saveCompetitions, mock_saveClubs, mock_loadCompetitions, mock_loadClubs):
        response = self.app.get('/book/Invalid Competition/Simply Lift')
        self.assertEqual(response.status_code, 302) 

        response = self.app.get('/book/Spring Festival/Invalid Club')
        self.assertEqual(response.status_code, 302)

    @patch('server.loadClubs', return_value=[{'name': 'Club A'}, {'name': 'Club B'}])
    @patch('server.loadCompetitions', return_value=[{'name': 'Competition A'}, {'name': 'Competition B'}])
    @patch('server.saveClubs')
    @patch('server.saveCompetitions')
    def test_purchase_places_invalid_club_or_competition(self, mock_saveCompetitions, mock_saveClubs, mock_loadCompetitions, mock_loadClubs):
        response = self.app.post('/purchasePlaces', data={'competition': 'Invalid Competition', 'club': 'Simply Lift', 'places': '3'})
        self.assertEqual(response.status_code, 302)  

        response = self.app.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Invalid Club', 'places': '3'})
        self.assertEqual(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()
