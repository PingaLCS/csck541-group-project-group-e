"""
This is the server-side coding and handles TWO functions.
1. One listener is used to receive the dictionary sent from the client side.
Deserialize the dictionary and support the print of the content or save the content to a txt file.
2. One listener is used to receive the content of the file sent from the client side. 
Support to input the decrypt key to decrypt the file's content and save it on the server side or 
save it in a non-decrypted txt file.
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


def deserialize_dict(serialization_format, serialized_dict):
    """
    Deserialize dictionary
    Support 3 types, binary, JSON, XML
    Return dictionary
    """
    try:
        if serialization_format == 'binary':
            return pickle.loads(serialized_dict)
        elif serialization_format == 'JSON':
            return json.loads(serialized_dict.decode())
        elif serialization_format == 'XML':
            root = ET.fromstring(serialized_dict)
            dictionary = {}
            for element in root.iter():
                if element.tag != 'dictionary':
                    dictionary[element.tag] = element.text
            return dictionary
    except Exception as e:
        print(f"An error occurred when deserialize dictionary: {e}")


def print_contents(dict, print_to_screen):
    """
    Print the content
    """
    if print_to_screen == 'y':
        print(f'Received dictionary: {dict}')


def save_files(dict, serialization_format, print_to_file):
    """
    Print the content to txt file and save it
    File will save in the same path of server.py
    """
    try:
        if print_to_file == 'y' and dict is not None:
            filename = input("Enter file name you want to save: ")
            with open(os.path.join(sys.path[0], filename), 'w') as f:
                f.write(str(dict))
                f.close
                print(
                    f"File '{filename}' is saved in the folder of 'Server Side'")
    except IOError as e:
        print(f"Failed to create and save file: {e}")


def receive_dictionary(serialization_format, host, port):
    """
    Receive the dictionary sent from client side
    Call deserialize_dict function
    Return dictionary
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print("Server is listening..............")
            conn, addr = s.accept()
            with conn:
                data = conn.recv(4096)
                dictionary = deserialize_dict(serialization_format, data)
                return dictionary
    except Exception as e:
        print(f"An error occurred when receive dictionary: {e}")


def receive_file(host, port):
    """
    Receive the file sent from the client side.
    Ask the user to input the file name.
    Ask the user decrypt the content or not, and run decrypt_content function if yes.
    The file will save in the same path of server.py.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print("Server is listening..............")
            conn, addr = s.accept()
            with conn:
                data = conn.recv(4096)
                file_content = pickle.loads(data)
                filename = input("Enter file name you want to save: ")
                decrypt = input("Decrypt file content? (y/n): ")
                with open(os.path.join(sys.path[0], filename), 'w') as f:
                    if decrypt == 'y':
                        decrypt_key = input("Enter decrypt key (MUST be 32 url-safe base64-encoded bytes): ")
                        file_content = decrypt_content(
                            file_content, decrypt_key)
                    f.write(file_content)
                    f.close
                    print(
                        f"File '{filename}' is saved in the folder of 'Server Side'")
    except Exception as e:
        print(f"An error occurred when receive file: {e}")


def decrypt_content(file_content, decrypt_key):
    """
    Decrypt and return the content
    """
    try:
        # Create Fernet object with key
        cipher = Fernet(decrypt_key)
        # Encrypt file content
        plaintext = cipher.decrypt(
            file_content.encode('utf-8')).decode('utf-8')
        return plaintext
    except Exception as e:
        print(f"An error occurred when decryptcontent: {e}")


def main():
    """
    Drive the main function to run the server side.
    Support user to choose to receive dictionary or file.
    """
    try:
        while True:
            item_type = input(
                "Enter '1' to receive a dictionary or '2' to receive a file: ")
            if item_type == '1':
                serialization_format = input(
                    "Enter serialization format (binary, JSON or XML): ")
                dictionary = receive_dictionary(
                    serialization_format, HOST, PORT)
                # call print function if yes
                print_to_screen = input("Received the message, print to screen? (y/n): ")
                print_contents(dictionary, print_to_screen)
                # call save function if yes
                print_to_file = input("Print and save to file? (y/n): ")
                save_files(dictionary, serialization_format, print_to_file)
            elif item_type == '2':
                receive_file(HOST, PORT)
                print("File received and decrypted.")
            else:
                print("Invalid input. Please enter '1' or '2'.")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")


if __name__ == '__main__':
    main()
