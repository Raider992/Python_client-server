import json
from jsonschema import validate

import unittest

from client import form_auth_message, form_presence_message


class TestClientFunc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.auth_msg = form_auth_message()
        self.prc_msg = form_presence_message()

        self.prc_schema = {
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "time": {"type": "number"},
                "type": {"type": "string"},
                "user": {"type": "object"}
            }
        }

        self.auth_schema = {
            "type": "object",
            "properties": {
                "action": {"type": "string"},
                "time": {"type": "number"},
                "type": {"type": "string"},
                "user": {"type": "object"}
            }
        }

    @classmethod
    def tearDownClass(self):
        print('tear_down')

    def is_json_valid(self, msg):
        try:
            json_object = json.loads(msg)
        except ValueError as e:
            return False
        return True

    def is_json_structure_valid(self, msg, schema):
        msg1 = json.loads(msg)
        try:
            validate(msg1, schema)
        except ValueError as e:
            return False
        return True

    def test_auth_message_is_json(self):
        print('test_auth_message_is_json')
        self.assertEqual(self.is_json_valid(self.auth_msg), True)

    def test_presence_message_is_json(self):
        print('test_presence_message_is_json')
        self.assertEqual(self.is_json_valid(self.prc_msg), True)

    def test_auth_message_data_structure(self):
        print('test_auth_message_data_structure')
        self.assertEqual(self.is_json_structure_valid(self.auth_msg, self.auth_schema), True)

    def test_presence_message_data_structure(self):
        print('test_presence_message_data_structure')
        self.assertEqual(self.is_json_structure_valid(self.prc_msg, self.prc_schema), True)


if __name__ == '__main__':
    unittest.main()
