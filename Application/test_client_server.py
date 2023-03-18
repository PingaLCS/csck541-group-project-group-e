import unittest
import Client_Side.client
import Server_Side.server
import os
import sys
import io
from unittest.mock import patch


class TestClientServer(unittest.TestCase):
    """
    This is the simple unit test and focus on the functions in client.py and server.py
    Server connection will not provide in unit test
    """

    def test_serialize_deserialize_dict_binary(self):
        """
        Test the function serialize_dict() of client.py in binary.
        Test the function deserialize_dict() of server.py in binary.
        """
        data = {'key': 'value'}
        serialized_data = Client_Side.client.serialize_dict('binary', data)
        deserialized_data = Server_Side.server.deserialize_dict(
            'binary', serialized_data)
        self.assertEqual(data, deserialized_data)

    def test_serialize_deserialize_dict_JSON(self):
        """
        Test the function serialize_dict() of client.py in JSON.
        Test the function deserialize_dict() of server.py in JSON.
        """
        data = {'key': 'value'}
        serialized_data = Client_Side.client.serialize_dict('JSON', data)
        deserialized_data = Server_Side.server.deserialize_dict(
            'JSON', serialized_data)
        self.assertEqual(data, deserialized_data)

    def test_serialize_deserialize_dict_XML(self):
        """
        Test the function serialize_dict() of client.py in XML.
        Test the function deserialize_dict() of server.py in XML.
        """
        data = {'key': 'value'}
        serialized_data = Client_Side.client.serialize_dict('XML', data)
        deserialized_data = Server_Side.server.deserialize_dict(
            'XML', serialized_data)
        self.assertEqual(data, deserialized_data)

    @patch('builtins.input', side_effect=['client_test.txt', 'test content', 'y', 'NoPNbKq2NPZI4iFIhFs9uSXVAvBkQEGYZvGB_LmNgbA='])
    def test_client_create_file(self, mock_input):
        """
        Test the function create_file() of client.py.
        The test include encrypt function.
        """
        Client_Side.client.create_file()
        # Check that file was created
        self.assertTrue(os.path.isfile(
            os.path.join(sys.path[0], 'client_test.txt')))

    def test_server_print_contents(self):
        """
        Test the function print_contents() of server.py.
        """
        dict = {'key': 'value'}
        print_to_screen = 'y'
        # capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        Server_Side.server.print_contents(dict, print_to_screen)
        sys.stdout = sys.__stdout__
        # check whether the print value has the vlaue of dict
        self.assertIn(str(dict), captured_output.getvalue())

    @patch('builtins.input', side_effect=['server_test.txt'])
    def test_server_save_file(self, mock_input):
        """
        Test the function save_files() of server.py.
        """
        dict = {'key': 'value'}
        print_to_file = 'y'
        Server_Side.server.save_files(dict, print_to_file)
        # Check that file was created
        self.assertTrue(os.path.isfile(
            os.path.join(sys.path[0], 'server_test.txt')))

    def test_server_decrypt_content(self):
        """
        Test the function decrypt_content() of server.py.
        """
        # read the content of file "client_test.txt"
        with open(os.path.join(sys.path[0], "client_test.txt"), "r") as file:
            content = file.read()
        decrypt_key = 'NoPNbKq2NPZI4iFIhFs9uSXVAvBkQEGYZvGB_LmNgbA='
        expected_result = 'test content'
        result = Server_Side.server.decrypt_content(content, decrypt_key)
        # check the content between expected result and result
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
