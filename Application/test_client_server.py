import unittest
import Client_Side.client
import Server_Side.server
import socket
import pickle
import json
import xml.etree.ElementTree as ET
from unittest.mock import patch
from io import StringIO
# Now, let's create a test class that inherits from unittest.TestCase:

# class TestClientServer(unittest.TestCase):
# Next, let's create test methods for each function you want to test. Here's an example of testing the deserialize_dict function:


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


if __name__ == '__main__':
    unittest.main()
