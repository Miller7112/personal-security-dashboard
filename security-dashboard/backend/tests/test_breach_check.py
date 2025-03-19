import unittest
from unittest.mock import patch
from utils.api_helpers import check_email_breach

class TestBreachCheck(unittest.TestCase):
    @patch('utils.api_helpers.requests.get')
    def test_email_breach_found(self, mock_get):
        """Test API response when an email is found in a breach."""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"Name": "TestBreach"}]

        result = check_email_breach("test@example.com")
        self.assertEqual(result[0]["Name"], "TestBreach")

    @patch('utils.api_helpers.requests.get')
    def test_email_breach_not_found(self, mock_get):
        """Test API response when no breach is found."""
        mock_get.return_value.status_code = 404

        result = check_email_breach("safe@example.com")
        self.assertIsNone(result)

    @patch('utils.api_helpers.requests.get')
    def test_api_error(self, mock_get):
        """Test API error handling."""
        mock_get.return_value.status_code = 500

        result = check_email_breach("error@example.com")
        self.assertIn("error", result)
