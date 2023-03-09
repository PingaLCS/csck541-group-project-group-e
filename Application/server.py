import socket
import pickle
import json
import xml.etree.ElementTree as ET

HOST = 'localhost'
PORT = 5000

def receive_data(conn):
    data = conn.recv(1024)
    return data

def deserialize_data(data, format):
    if format == 'binary':
        return pickle.loads(data)
    elif format == 'JSON':
        return json.loads(data)
    elif format == 'XML':
        root = ET.fromstring(data)
        my_dict = {}
        for child in root:
            my_dict[child.tag] = child.text
        return my_dict

def print_to_screen(data):
    print(data)

def print_to_file(data, filename):
    with open(filename, 'w') as f:
        f.write(data)

def handle_data(data):
    try:
        format = input("Enter deserialization format (binary, JSON or XML): ")
        deserialized_data = deserialize_data(data, format)
        print_choice = input("Enter print choice (1: print to screen, 2: print to file, 3: both): ")
        if print_choice == '1':
            print_to_screen(deserialized_data)
        elif print_choice == '2':
            filename = input("Enter file name: ")
            print_to_file(str(deserialized_data), filename)
        elif print_choice == '3':
            print_to_screen(deserialized_data)
            filename = input("Enter file name: ")
            print_to_file(str(deserialized_data), filename)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = receive_data(conn)
                handle_data(data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()