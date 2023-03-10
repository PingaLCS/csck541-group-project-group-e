import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

HOST = 'localhost'
PORT = 5000

# Set the key for encryption and decryption
key = "NoPNbKq2NPZI4iFIhFs9uSXVAvBkQEGYZvGB_LmNgbA="
#key = Fernet.generate_key()

def create_dict():
    my_dict = {}
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value
    return my_dict

def serialize_dict(my_dict):
    format = input("Enter serialization format (binary, JSON or XML): ")
    if format == 'binary':
        return pickle.dumps(my_dict)
    elif format == 'JSON':
        return json.dumps(my_dict).encode('utf-8')
    elif format == 'XML':
        root = ET.Element("root")
        for key, value in my_dict.items():
            node = ET.SubElement(root, key)
            node.text = value
        return ET.tostring(root)

def create_file():
    try:
        filename = input("Enter file name: ")
        content = input("Enter file content: ")
        encrypt = input("Encrypt file content? (y/n): ")
        if encrypt == 'y':
            # Create Fernet object with key
            cipher_suite = Fernet(key)
            # Encrypt file content
            content = cipher_suite.encrypt(content.encode('utf-8')).decode('utf-8')
        with open(filename, 'w') as f:
            f.write(content)
        return content
    except IOError as e:
        print(f"Failed to create file: {e}")

def send_data(serialized_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall("1")
            s.sendall(serialized_data)
    except ConnectionRefusedError:
        print("Connection refused. Server may not be running.")

def send_file(serialized_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            #s.sendall(key)
            s.sendall("2")
            s.sendall(serialized_data)
    except ConnectionRefusedError:
        print("Connection refused. Server may not be running.")

def main():
    try:
        choice = input("Enter choice (1: create dictionary, 2: create file) and send to server: ")
        if choice == '1':
            my_dict = create_dict()
            serialized_data = serialize_dict(my_dict)
            send_data(serialized_data)
        elif choice == '2':
            my_file = create_file()
            send_file(my_file)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()