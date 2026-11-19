import unittest
from modules.validators import validate_username, analyze_email_syntax


class ValidatorTests(unittest.TestCase):
    def test_valid_username(self):
        self.assertEqual(validate_username("sali_123"), (True, "sali_123"))

    def test_username_trims_spaces(self):
        self.assertEqual(validate_username("  sali  "), (True, "sali"))

    def test_empty_username(self):
        self.assertFalse(validate_username("")[0])

    def test_invalid_username_characters(self):
        self.assertFalse(validate_username("name with spaces")[0])

    def test_email_syntax(self):
        result = analyze_email_syntax("person@example.com")
        self.assertTrue(result["valid_syntax"])
        self.assertEqual(result["domain"], "example.com")

    def test_invalid_email(self):
        self.assertFalse(analyze_email_syntax("not-an-email")["valid_syntax"])


if __name__ == "__main__":
    unittest.main()
