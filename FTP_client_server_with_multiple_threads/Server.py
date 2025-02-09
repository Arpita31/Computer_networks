import socket
import os
import threading

def send_file(connection, file_name):
    '''
        Function to send a file to the client
        Args:
            connection: Connection socket dedicated to a client
            file_name: Sending file name
    '''
    try:
        with open(file_name, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                connection.sendall(chunk)
        connection.sendall(b"EOF")
        print(f"Successfully sent {file_name}.")
    except Exception as e:
        print(f"Error sending file: {e}")

def receive_file(connection, file_name):
    '''
        Function to receive a file from the client.
        Args:
            connection: Connection socket dedicated to a client
            file_name: Receiving file name
    '''
    try:
        with open(file_name, 'wb') as file:
            while True:
                data = connection.recv(1024)
                if data.endswith(b"EOF"):
                    file.write(data[:-3])
                    break
                file.write(data)
        print(f"Successfully received {file_name}.")
    except Exception as e:
        print(f"Error receiving file: {e}")

def handle_client(connection, addr):
    '''
        This function handles connected client's operations (get/upload).
        Args:
            connection: Connection socket dedicated to a client
    '''
    print(f"New connection accepted from {addr}")
    try:
        while True:
            client_command = connection.recv(1024).decode()
            if not client_command or client_command.lower() == "exit":
                print(f"Terminated connection from {addr}")
                break

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
        connection.close()


def ftp_server():
    '''
        This function runs the FTP server capable of handling multiple clients.
    '''
    HOST = 'localhost'
    PORT = 5106

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")
        
        while True:
            try:
                connection, addr = server_socket.accept()
                # Handle each client in a new thread
                client_thread = threading.Thread(target=handle_client, args=(connection, addr))
                client_thread.start()
            except Exception as e:
                print(f"Server error: {e}")

if __name__ == "__main__":
    ftp_server()
