import socket
import sys

def send_file(client_socket, file_name):
    '''
        Function to send a file to the server
        Args:
            client_socket: Socket to connect with server
            file_name: Sending file name
    '''
    try:
        # open file in binary read mode
        with open(file_name, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                client_socket.sendall(chunk)

        # After last chunk of the file, send EOF 
        client_socket.sendall(b"EOF")
        print(f"{file_name} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload {file_name}: {e}")

def receive_file(client_socket, file_name):
    '''
        Function to receive a file from server.
        Args:
            connection: Connection socket dedicated to a client
            file_name: receiving file name
    '''
    try:
        # Open file in binary write mode
        with open(file_name, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if data.endswith(b"EOF"):  # Check for EOF signal
                    file.write(data[:-3])  # exclude EOF and add data
                    break
                file.write(data)
        print(f"File {file_name} downloaded successfully.")
    except Exception as e:
        print(f"Failed to download {file_name}: {e}")

def ftp_client(sPort):
    '''
        This function runs the FTP client
        Args:
            sPort: Port number for connecting to the server
    '''
    server_host = 'localhost'

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as requestSocket:
            requestSocket.connect((server_host, sPort))
            print("Connected to server.")

            while True:
                # User's action inputs
                client_command = input("Enter command: \n1. upload <file_name> \n2. get <file_name> \n3. exit\n:  ")
                if client_command.lower() == "exit":
                    requestSocket.sendall(b"exit")
                    break

                action, file_name = client_command.split(maxsplit=1)
                requestSocket.send(f"{action} {file_name}".encode())

                # Server's response on users action
                response = requestSocket.recv(1024).decode()
                if response == "OK":
                    if action == "get":
                        # Receive a file from server
                        receive_file(requestSocket, f"new{file_name[0].upper()}{file_name[1:]}")
                    elif action == "upload":
                        # Send a File to server
                        send_file(requestSocket, file_name)
                else:
                    print("Server response:", response)
    except Exception as e:
        print(f"Client error: {e}")

if __name__ == "__main__":
    # Specify the Port number with command line argumnts
    if len(sys.argv) != 2:
        print("Usage: python ftpclient.py <port>") 
        sys.exit(1)
    sPort = int(sys.argv[1])
    ftp_client(sPort)
