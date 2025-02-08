import socket
import os

def send_file(connection, file_name):
    '''
        Function to send a file to the client
        Args:
            connection: Connection socket dedicated to a client
            file_name: Sending file name
    '''
    try:
        # open file in binary read mode
        with open(file_name, 'rb') as file:
            # send chunks of 1024 bytes
            for chunk in iter(lambda: file.read(1024), b''):
                connection.sendall(chunk)

        # After last chunk of the file, send EOF 
        connection.sendall(b"EOF")
        print(f"Successfully sent {file_name}.")
    except Exception as e:
        print(f"Error sending file: {e}")

def receive_file(connection, file_name):
    '''
        Function to receive a file from client.
        Args:
            connection: Connection socket dedicated to a client
            file_name: receiving file name
    '''
    try:
        # Open file in binary write mode
        with open(file_name, 'wb') as file:
            while True:
                data = connection.recv(1024)
                if data.endswith(b"EOF"):  # Check for EOF signal
                    file.write(data[:-3])  # exclude EOF and add data
                    break
                file.write(data)
        print(f"Successfully received {file_name}.")
    except Exception as e:
        print(f"Error receiving file: {e}")

def handle_client(connection):
    '''
        This function handles connected clients operations get/upload
        Args:
            connection: Connection socket dedicated to a client
    '''
    try:
        while True:
            # Receive client's command
            client_command = connection.recv(1024).decode()
            if not client_command or client_command.lower() == "exit":
                break  # Exit loop for 'exit' command

            # Separat action and filename
            action, file_name = client_command.split(maxsplit=1)
            
            if action == "get":
                if os.path.exists(file_name):
                    connection.send(b"OK")
                    send_file(connection, file_name)
                else:
                    connection.send(b"ERROR: File not found.")
                    
            elif action == "upload":
                connection.send(b"OK")
                receive_file(connection, f"new{file_name[0].upper()}{file_name[1:]}")
            else:
                connection.send(b"ERROR: Invalid command.")
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        # Close the connection after completion of tasks
        connection.close()

def ftp_server():
    '''
        This function runs the FTP server
    '''
    sSocket = 'localhost'
    sPort = 5106

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Starts a listening socket at the sSocket and sPort
        server_socket.bind((sSocket, sPort))
        server_socket.listen()
        print(f"Server listening on port {sPort}")
        
        while True:
            try:
                # creates a dedicated connection for client
                connection, addr = server_socket.accept()
                print("New connection accepted.")
                handle_client(connection)
            except Exception as e:
                print(f"Server error: {e}")

if __name__ == "__main__":
    ftp_server()
