import socket
from time_synchronization import get_time_string

host = 'localhost'
port = 9901

def save_to_file(sender, message):
    timestamp = get_time_string()
    with open("chat_file.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]{sender}: {message}\n")

def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server is listening on {host}: {port}")

    try:
        conn, address = server_socket.accept()
        print(f"Client connected from {address}")

        while True:
            # receive message form client
            data = conn.recv(1024).decode('utf-8')
            # if client disconnect
            if not data:
                break

            print(f"Client: {data}")
            save_to_file("Client", data)

            # get input from server and send to client
            message = input("Server: ")
            conn.sendall(message.encode('utf-8'))
            save_to_file("Server", message)
    except socket.error as e:
        print(f"Connection error: {e}")
    finally:
        conn.close()
        server_socket.close()

def chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Connected to the server {host}: {port}")

        while True:
            # get input from client and send to server
            sent_message = input("Client: ")
            client_socket.sendall(sent_message.encode('utf-8'))
            save_to_file("Client", sent_message)

            # receive message from server
            received_data = client_socket.recv(1024).decode('utf-8')
            # if server disconnect
            if not received_data:
                break
            print(f"Server: {received_data}")
            save_to_file("Server", received_data)
    except socket.error as e:
        print(f"Connection error: {e}")
    finally:
        client_socket.close()

if __name__ == '__main__':
    print("1. Run as server")
    print("2. Run as client")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        chat_server()
    elif choice == '2':
        chat_client()
    else:
        print("Invalid choice.")
