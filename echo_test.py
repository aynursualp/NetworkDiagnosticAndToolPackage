import socket

host = 'localhost'
port = 9900

def echo_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # enable port reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server is listening on {host}: {port}")

    while True:
        conn, address = server_socket.accept()
        # receive bytes and decode to string
        data = conn.recv(1024).decode('utf-8')

        if data:
            print(f"Received from client {address}: {data}")
            # encode string back to bytes
            conn.sendall(data.encode('utf-8'))

        conn.close()

def echo_client():
    message = "Test message"
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        # encode string to bytes
        client_socket.sendall(message.encode('utf-8'))
        # receive bytes and decode to string
        received_data = client_socket.recv(1024).decode('utf-8')

        print(f"Sent: {message}")
        print(f"Received: {received_data}")

        # compare sent and received data
        if message == received_data:
            print("Connection successful, data matches")
        else:
            print("Data mismatch")

    except socket.error as e:
        print(f"Connection error: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    echo_server()
    echo_client()