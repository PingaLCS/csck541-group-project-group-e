import socket
import pickle
import json
import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

HOST = 'localhost'
PORT = 5000

# Set the key for encryption and decryption
key = "NoPNbKq2NPZI4iFIhFs9uSXVAvBkQEGYZvGB_LmNgbA="

def deserialize_data(serialized_data, format):
    if format == 'binary':
        return pickle.loads(serialized_data)
    elif format == 'JSON':
        return json.loads(serialized_data.decode('utf-8'))
    elif format == 'XML':
        root = ET.fromstring(serialized_data, parser=ET.XMLParser(encoding="utf-8"))
        my_dict = {}
        for node in root:
            my_dict[node.tag] = node.text
        return my_dict

def save_file(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
    except Exception as e:
        print(e)

def decrypt_content(content):
    # Create Fernet object with key
    cipher_suite = Fernet(key)
    # Decrypt content
    return cipher_suite.decrypt(content.encode('utf-8')).decode('utf-8')

def handle_data(data):
    try:
        # Choose serialization format
        format = input("Enter serialization format (binary, JSON or XML): ")
        
        # Deserialize data
        my_dict = deserialize_data(data, format)
        # Print contents of dictionary
        print(my_dict)
        # Choose whether to save file
        save_file_option = input("Save file? (y/n): ")
        if save_file_option == 'y':
            filename = input("Enter file name: ")
            content = input("Enter file content: ")
            encrypt = input("Encrypt file content? (y/n): ")
            if encrypt == 'y':
                content = decrypt_content(content)
            save_file(filename, content)
    except Exception as e:
        print(e)

def handle_file(key, data):
    try:
        # create a Fernet object with the key
        fernet = Fernet(key)

        if key is not None:
            # decrypt the data
            decrypted_data = fernet.decrypt(data)
        else:
            decrypted_data = data
        
        # save the decrypted data to a file
        with open('received_file.txt', 'wb') as file:
            file.write(decrypted_data)

    except Exception as e:
        print(e)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # bind the socket to the server address
        s.bind((HOST, PORT))
        # listen for incoming connections
        s.listen()
        # accept a connection
        print('Waiting for a connection...')
        conn, addr = s.accept()
        print('Connected to', addr)
        with conn:
            action_no = conn.recv(4096)
            data = conn.recv(4096)
            if action_no == "1":
                handle_data(data)
            #key = conn.recv(1024)
            #filedata = conn.recv(1024)
            #if filedata is not None:
             #   handle_file(key, filedata)
        
        # close the socket
        conn.close()




if __name__ == '__main__':
    main()