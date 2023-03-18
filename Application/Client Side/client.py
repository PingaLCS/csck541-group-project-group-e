"""
This is the client-side coding and handles TWO functions.
1. One is send the dictionary to the server side.
Serialize the dictionary and support user choose 3 types.
2. One is create a file in local (folder of "Client Side") and 
send the content of the file to the server side. 
Support to input the encrypt key to encrypt the file's content and save it on the client side or 
save it in a non-encrypted txt file.
"""
import socket
import pickle
import json
import os
import sys
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

# Set the local host and port
HOST = 'localhost'
PORT = 5000


def serialize_dict(serialization_format, dictionary):
    """
    Serialize the dictionary
    Support 3 types, binary, JSON, XML
    Return dictionary
    """
    try:
        if serialization_format == 'binary':
            return pickle.dumps(dictionary)
        elif serialization_format == 'JSON':
            return json.dumps(dictionary).encode()
        elif serialization_format == 'XML':
            root = ET.Element('dictionary')
            for key, value in dictionary.items():
                element = ET.SubElement(root, key)
                element.text = str(value)
            return ET.tostring(root)
        else:
            raise ValueError(f"Unsupported serialization format {serialization_format}")
    except Exception as e:
        print(f"An error occurred when serialize dictionary: {e}")



def send_dictionary(dictionary, serialization_format, host, port):
    """
    Send dictionary to the server side
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            data = serialize_dict(serialization_format, dictionary)
            s.sendall(data)
    except ConnectionRefusedError:
        print("Connection refused. Server may not be running.")


def send_file(file_data, host, port,):
    """
    Send content of file to the server side
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            file_data = pickle.dumps(file_data)
            s.sendall(file_data)
    except ConnectionRefusedError:
        print("Connection refused. Server may not be running.")


def create_file():
    """
    Create a txt file
    Users can input the file name and enter the content for the txt file
    Users can encrypt the content with an inputed key
    The file will save in the same path of client.py
    """
    try:
        filename = input("Enter file name: ")
        file_content = input("Enter file content: ")
        encrypt = input("Encrypt file content? (y/n): ")
        if encrypt == 'y':
            encrypt_key = input("Enter encrypt key: ")
            # Create Fernet object with key
            cipher_suite = Fernet(encrypt_key)
            # Encrypt file content
            file_content = cipher_suite.encrypt(
                file_content.encode('utf-8')).decode('utf-8')
        with open(os.path.join(sys.path[0], filename), 'w') as f:
            f.write(str(file_content))
        return file_content
    except IOError as e:
        print(f"Failed to create file: {e}")


def main():
    """
    Drive the main function to run the function of client side.
    Support user to choose to send dictionary or file.
    """
    try:
        while True:
            item_type = input(
                "Enter '1' to send a dictionary or '2' to send a file: ")
            if item_type == '1':
                my_dict = {}
                while True:
                    key = input("Enter a key or 'q' to quit: ")
                    if key == 'q':
                        break
                    value = input("Enter a value: ")
                    my_dict[key] = value
                serialization_format = input(
                    "Enter serialization format (binary, JSON or XML): ")
                send_dictionary(my_dict, serialization_format, HOST, PORT)
            elif item_type == '2':
                my_file = create_file()
                send_file(my_file, HOST, PORT)
            else:
                print("Invalid input. Please enter '1' or '2'.")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == '__main__':
    main()
