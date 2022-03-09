from django.test import TestCase
import json

# Create your tests here.


class DecryptionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        This function is run before all the tests
        """
        f = open("unit_tests.json")
        cls.data = json.load(f)
        cls.success_message = {"DecryptedMessage": "Nice work!\n"}
        cls.failed_decryption = {"Error": "Decryption Failed !"}
        cls.missing_message = {
            "message": [
                "This field is required"
            ]
        }
        cls.missing_passphrase = {
            "passphrase": [
                "This field is required"
            ]
        }

    def test_other_urls(self):
        """
        GET / returns status code 404 (only /decryptedMessage/ works)
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_get_method(self):
        """
        This function tests the get method of the decryptMessage view
        GET /decryptedMessage/ returns status code 405 (only post request allowed)
        """
        response = self.client.get('/decryptMessage/')
        self.assertEqual(response.status_code, 405)

    def test_success_decryption(self):
        """
        This function tests the success case of the decryption function
        POST /decryptedMessage/ returns status code 200 and encrypted message
        """
        response = self.client.post('/decryptMessage/', self.data[0])
        self.assertEqual(response.data, self.success_message)
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_incorrect_passphrase(self):
        """
        This function tests the case where the passphrase is incorrect
        POST /decryptedMessage/ returns status code 400 
        """
        response = self.client.post('/decryptMessage/', self.data[1])
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.failed_decryption)

    def test_missing_passphrase(self):
        """
        This function tests the case where the passphrase is missing
        POST /decryptedMessage/ returns status code 400
        """
        response = self.client.post('/decryptMessage/', self.data[2])
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.missing_passphrase)

    def test_missing_message(self):
        """
        This function tests the case where the message is missing
        POST /decryptedMessage/ returns status code 400
        """
        response = self.client.post('/decryptMessage/', self.data[3])
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, self.missing_message)
