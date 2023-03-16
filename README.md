# Group Project - Group E, CSCK541-Software Development in Practice Jan 2023 B
This is a Group Project (Group E). 

Created by : 
  -  Pinga Lau Chi Shing, MSc Data Science and Artificial Intelligence student.
  -  Murphy Luke, MSc Data Science and Artificial Intelligence student.
  -  Hao Guanzhong, MSc Data Science and Artificial Intelligence student.
Submitted to The University of Liverpool.

## The requirement of the project for programming 
Build a simple client/server network, including functions and features here.
  1.  The client and server can be on separate or the same machine.
  2.  Write to PEP standards.
  3.  Include the exception handling
  4.  Write unit tests for each function.
  5.  Include a directory tree.
  6.  Include a Readme.md and dependencies.txt / requirements.txt.
Client side's functions:
  1.  Create a dictionary, populate it, serialize it and send it to the server.
        -  Create and send a dictionary to the server side.
        -  Able to set the pickling format to one of the following: binary, JSON or XML.
  2.  Create a text file and send it to the server.
        -  Create and save the text file to the client side.
        -  Send the content of the file to the server side.
        -  Support users to have the option to encrypt the text in a text file.
Server Side's functions:
  1.  Open a listener to receive the dictionary sent from the client side.
        -  Deserialize the dictionary.
        -  Support users with a configurable option to print the contents to the screen.
        -  Support users with a configurable option to save the content in a text file.
  2.  Open a listener to receive the content of the file sent from the client side.
        -  Support users to have the option to decrypt the text in a text file.

## Usage (steps)
Before run the program: 
  1.  Base on the file `requirements.txt` to ensure you install the related package.
  2.  Prepare TWO virtual environments to run the python program, `client.py` and `server.py`.
Main function 1 - Create a dictionary and send it to the server side:
  1.  [Server-side] Run the server-side virtual environment and locate the file `server.py` path.
  2.  [Server-side] Type `python server.py` to run the program.
  3.  [Server-side] Enter `1` to receive a dictionary and select the serialization  format to start the listener.
  4.  [Server-side] Show `Server is listening...............` on the screen.
  5.  [Client-side] Run the client-side virtual environment and locate the file `client.py` path.
  6.  [Client-side] Type `python client.py` to run the server program.
  7.  [Client-side] Enter `1` to send a dictionary.
  8.  [Client-side] Enter a key and value, for example, `Name` with `Pinga`.
  9.  [Client-side] It supports multiple keys so that we can enter the second key, like `Age` with `30`.
  10. [Client-side] Enter `q` to quit when finish the dictionary.
  11. [Client-side] Enter the serialization format for the dictionary. It MUST be the same as your selection on the server side.
  12. [Server-side] Server side will receive the dictionary and ask you to print it to the screen.
  13. [Server-side] Show the result in the screen if you enter `y` like `{'Name': 'Pinga', 'Age': '30'}`
  14. [Server-side] Ask you to print and save the content to file.
  15. [Server-side] Ask you to enter the file name, for example, `dictionary_json.txt`.
  16. [Server-side] Show `File 'dictionary_json.txt' is saved in the folder of 'Server Side'`.
  17. The file will save in the same path as the file `server.py`.
Main function 2 - Create a text file and send it to the server:
  1.  [Server-side] Enter `2` to receive the content of file.
  2.  [Server-side] Show `Server is listening...............` on the screen.
  3.  [Client-side] Enter `2` to create and send a file.
  4.  [Client-side] Ask you to enter the file name, for example, `client_file.txt`.
  5.  [Client-side] Ask you to enter the file content, for example, `This is our group project, we are group E.`.
  6.  [Client-side] Ask to encrypt file content or not. 
  7.  [Client-side] Ask for the encryption key if you enter `y`.
  8.  [Client-side] Enter a 32 url-safe base64-encoded bytes key. You can use the Fernet to generate a key online or use this:
                    Fernet Key = `NoPNbKq2NPZI4iFIhFs9uSXVAvBkQEGYZvGB_LmNgbA=`
  10. [Client-side] Show `File is created and sent to server.`, then switch to the server side.
  11. The file will save in the same path as the file `client.py` and the content is encrypted.
  12. [Server-side] Server side will receive the request and ask you to enter the file name you want, for example, `server_file.txt`
  13. [Server-side] Ask you to decrypt the file. The content will be encrypted if no.
  14. [Server-side] If yes, the system will ask you the enter the decrypt key. It MUST be the same as the encrypted one.
  15. [Server-side] Show `File 'server_file.txt' is saved in the folder of 'Server Side'`.
  16. The file will save in the same path as the file `server.py`.

## License
[MIT] Copyright (c) 2023 Pinga Lau Chi Shing, Murphy Luke, Hao Guanzhong