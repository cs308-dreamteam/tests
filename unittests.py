import unittest
import requests
import time
from faker import Faker
from connect import create_connection
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.environ.get('ACCESS_TOKEN')

mock = Faker().name()
mock2 = Faker().name()
connection = create_connection()

class UnitTestClass(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:3000"
        self.headers = {
            'Content-Type': 'application/json',
            'x-access-token': access_token
        }
        self.fakename = mock
        self.fakename2 = mock2


    def test_invalid_auth_token(self):
        headers = {'Content-Type': 'application/json', 'x-access-token': 'invalid_token'}
        response = requests.get(f"{self.base_url}/getRecommendations", headers=headers)
        self.assertNotEqual(response.status_code, 201, "Status code should not be 201 with invalid token")

    def test_response_time_for_recom(self):
        start_time = time.time()
        response = requests.get(f"{self.base_url}/getRecommendations", headers=self.headers)
        end_time = time.time()
        self.assertTrue((end_time - start_time) < 5, "Response time should be less than 5 second")

    def test_empty_response_handling(self):
        response = requests.get(f"{self.base_url}/getRecommendations", headers=self.headers)
        self.assertIsNotNone(response.json(), "Response should not be None")

    def test_get_recommendation_return_types(self):
        response = requests.get(f"{self.base_url}/getRecommendations", headers=self.headers)
        self.assertEqual(response.status_code, 201, "Status code should be 201")

        data = response.json()
        self.assertIsInstance(data, dict, "Response should be a dictionary")

        # Test if the keys exist
        self.assertIn('friendRecommendations', data, "Response should contain friendRecommendations")
        self.assertIn('ourRecom', data, "Response should contain ourRecom")
        self.assertIn('spotifyRecom', data, "Response should contain spotifyRecom")

        # Test the structure of spotifyRecom data
        for item in data['spotifyRecom']:
            self.assertIn('song', item, "Each item should have a 'song' key")
            self.assertIn('artist', item, "Each item should have an 'artist' key")
            self.assertIn('album', item, "Each item should have an 'album' key")
            self.assertIn('genre', item, "Each item should have a 'genre' key")

            # Additional checks for the type of each field can be added here
            self.assertIsInstance(item['song'], str, "'song' should be a string")
            self.assertIsInstance(item['artist'], str, "'artist' should be a string")
            self.assertIsInstance(item['album'], str, "'album' should be a string")
            self.assertIsInstance(item['genre'], str, "'genre' should be a string")

        for item in data['friendRecommendations']:
            self.assertIn('song', item, "Each item should have a 'song' key")
            self.assertIn('artist', item, "Each item should have an 'artist' key")
            self.assertIn('album', item, "Each item should have an 'album' key")
            self.assertIn('genre', item, "Each item should have a 'genre' key")

            # Additional checks for the type of each field can be added here
            self.assertIsInstance(item['song'], str, "'song' should be a string")
            self.assertIsInstance(item['artist'], str, "'artist' should be a string")
            self.assertIsInstance(item['album'], str, "'album' should be a string")
            self.assertIsInstance(item['genre'], str, "'genre' should be a string")

        for item in data['ourRecom']["attributes"]:
            self.assertIn('song', item, "Each item should have a 'song' key")
            self.assertIn('artist', item, "Each item should have an 'artist' key")
            self.assertIn('album', item, "Each item should have an 'album' key")
            self.assertIn('genre', item, "Each item should have a 'genre' key")

            # Additional checks for the type of each field can be added here
            self.assertIsInstance(item['song'], str, "'song' should be a string")
            self.assertIsInstance(item['artist'], str, "'artist' should be a string")
            self.assertIsInstance(item['album'], str, "'album' should be a string")
            self.assertIsInstance(item['genre'], str, "'genre' should be a string")

    def test_successful_recommendations_fetching(self):
        """
        Test that the /getRecommendations route successfully fetches recommendations.
        """
        response = requests.get(f"{self.base_url}/getRecommendations", headers=self.headers)
        self.assertEqual(response.status_code, 201, "Successful fetch should return status code 201")
        data = response.json()
        self.assertIn('friendRecommendations', data)
        self.assertIn('ourRecom', data)
        self.assertIn('spotifyRecom', data)

    def test_successful_rating_change(self):
        payload = {'new_rating': 5, 'song_name': 'Devil\'s Dance'}
        response = requests.post(f"{self.base_url}/changeRating", headers=self.headers, json=payload)
        self.assertEqual(response.status_code, 201)

    def test_unauthorized_access(self):
        headers = {'Content-Type': 'application/json', 'x-access-token': 'invalid_token'}
        payload = {'new_rating': 5, 'song_name': 'Valid Song Name'}
        response = requests.post(f"{self.base_url}/changeRating", headers=headers, json=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_invalid_request_body(self):
        payload = {'new_rating': 5}  # Missing song_name
        response = requests.post(f"{self.base_url}/changeRating", headers=self.headers, json=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_register_weak_password(self):
        payload = {'name': 'testUser', 'pass': 'weak', 'mail': 'testuser@example.com'}
        response = requests.post(f"{self.base_url}/register", params=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_send_verification_email(self):
        payload = {'userEmail': f'{self.fakename2}@example.com'}
        response = requests.post(f"{self.base_url}/send-verification-email", params=payload)
        self.assertEqual(response.status_code, 201)

    def test_send_verification_missing_email(self):
        response = requests.post(f"{self.base_url}/send-verification-email")
        self.assertNotEqual(response.status_code, 201)

    def test_verify_incorrect_code(self):
        payload = {'userCode': 'wrong_code', 'mail': f'{self.fakename}@example.com', 'user': self.fakename,
                   'pass': 'StrongPass123!'}
        response = requests.post(f"{self.base_url}/verify", params=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_verify_missing_user_details(self):
        payload = {'userCode': '1234', 'mail': f'{self.fakename}@example.com'}
        response = requests.post(f"{self.base_url}/verify", params=payload)
        self.assertNotEqual(response.status_code, 201)

    def test_verify_correct_code(self):
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT v.code FROM verification v WHERE v.email = '{self.fakename2}@example.com';")
        valid_code = cursor.fetchall()[0]['code']

        payload = {'userCode': valid_code, 'mail': f'{self.fakename2}@example.com', 'user': self.fakename2, 'pass': 'StrongPass123!'}
        response = requests.post(f"{self.base_url}/verify", params=payload)
        self.assertEqual(response.status_code, 201)
        cursor.close()
        connection.close()

    def test_follow_user_invalid_data(self):
        """
        Test following a user with invalid data.
        """
        payload = {'inputValue': ''}
        response = requests.post(f"{self.base_url}/follows", headers=self.headers, json=payload)
        self.assertNotEqual(response.status_code, 201, "Invalid data should not return status code 201")

    def test_follow_user_unauthorized(self):
        """
        Test following a user without proper authentication.
        """
        payload = {'inputValue': 'anotherUser'}
        response = requests.post(f"{self.base_url}/follows", json=payload)  # No headers
        self.assertNotEqual(response.status_code, 201, "Unauthorized request should not return status code 201")

    def test_delete_song_unauthorized(self):
        """
        Test deletion of a song without proper authentication.
        """
        payload = {'title': 'Valid Song Title'}
        response = requests.delete(f"{self.base_url}/delete_song", json=payload)  # No headers
        self.assertNotEqual(response.status_code, 200, "Unauthorized request should not return status code 200")

    def delete_song_successfully(self):
        """
            Test the successful deletion of a song.
        """
        payload = {"title": "Rolling in the Deep"}
        response = requests.delete(f"{self.base_url}/delete_song", headers=self.headers, json=payload)
        self.assertEqual(response.status_code, 200, "Deleting songs should return status code 200")
        cursor = connection.cursor()
        results = cursor.execute("SELECT * FROM SONGS WHERE songTitle = 'Rolling in the Deep';")
        self.assertTrue(len(results) > 0)


    def test_add_song_successfully(self):
        """
        Test the successful addition of a song list.
        """
        payload = {
            'songList': [
                {
                    'title': 'Dancing Queen',
                    'albums': ['Arrival'],
                    'artists': ['ABBA'],
                    'genres': ['Dance Pop'],
                    'rating': '5'
                }
            ]
        }
        response = requests.post(f"{self.base_url}/add_song", headers=self.headers, json=payload)
        self.assertEqual(response.status_code, 200, "Adding songs should return status code 200")

    def test_add_song_unauthorized(self):
        """
        Test addition of a song without proper authentication.
        """
        payload = {
            'songList': [
                {
                    'title': 'Dancing Queen',
                    'albums': ['Arrival'],
                    'artists': ['ABBA'],
                    'genres': ['Dance Pop'],
                    'rating': 5
                }
            ]
        }
        response = requests.post(f"{self.base_url}/add_song", json=payload)  # No headers
        self.assertNotEqual(response.status_code, 200, "Unauthorized request should not return status code 200")

    def test_get_top5_successfully(self):
        """
        Test successfully retrieving the top 5 songs for a user.
        """
        params = {'user': 'efe'}
        response = requests.get(f"{self.base_url}/get_top5", headers=self.headers, params=params)
        self.assertEqual(response.status_code, 201, "Retrieving top 5 songs should return status code 201")
        data = response.json()
        self.assertIn('songs', data, "Response should contain a 'songs' key")
        self.assertLessEqual(len(data['songs']), 5, "Response should contain less than or equal to 5 songs")

    def test_get_top5_unauthorized(self):
        """
        Test retrieving top 5 songs without proper authentication.
        """
        params = {'user': 'efe'}
        response = requests.get(f"{self.base_url}/get_top5", params=params)  # No headers
        self.assertNotEqual(response.status_code, 201, "Unauthorized request should not return status code 201")


if __name__ == '__main__':
    unittest.main()
