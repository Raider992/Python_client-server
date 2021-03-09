import json
from jsonschema import validate

import unittest

from server import form_auth_resp


class TestClientFunc(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.auth_msg = form_auth_resp()

        self.auth_resp_schema = {
            "type": "object",
            "properties": {
                "response": {"type": "number"},
                "alert": {"type": "string"}
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
        try:
            validate(msg, schema)
        except ValueError as e:
            return False
        return True

    def test_auth_response_is_json(self):
        print('test_auth_message_is_json')
        self.assertEqual(self.is_json_valid(self.auth_msg), True)

    def test_presence_message_is_json(self):
        print('test_presence_message_is_json')
        self.assertEqual(self.is_json_valid(self.auth_msg), True)


if __name__ == '__main__':
    unittest.main()
