import socket
import pickle
import json
import xml.etree.ElementTree as ET

HOST = 'localhost'
PORT = 5000

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
        return json.dumps(my_dict)
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
            content = encrypt_file(content)
        with open(filename, 'w') as f:
            f.write(content)
    except IOError as e:
        print(f"Failed to create file: {e}")

def encrypt_file(content):
    # Implement encryption algorithm here
    return content

def send_data(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(data)
    except ConnectionRefusedError:
        print("Connection refused. Server may not be running.")

def main():
    try:
        choice = input("Enter choice (1: create dictionary, 2: create file): ")
        if choice == '1':
            my_dict = create_dict()
            serialized_data = serialize_dict(my_dict)
            send_data(serialized_data)
        elif choice == '2':
            create_file()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()