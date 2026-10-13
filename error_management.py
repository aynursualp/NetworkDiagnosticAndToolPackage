import socket

SEND_BUFF_SIZE = 4096
RECV_BUFF_SIZE = 2048

def error_management():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_buf_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Send buffer size: ", send_buf_size)
    recv_buf_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Received buffer size: ", recv_buf_size)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)

    send_buf_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Modified send buffer size after: ", send_buf_size)
    recv_buf_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Modified recevied buffer size: ", recv_buf_size)


    sock.setblocking(False)
    print("Non blocking mode")
    sock.settimeout(3)
    print("Socket timeout: ", sock.gettimeout(), " seconds")

    print("Connection error attempt")
    try:
        sock.connect(('111.111.111.111', 80))
    except socket.timeout:
        print("Connection timeout")
    except socket.error as e:
        print(f"{e} Error")
    finally:
        sock.close()
        print("Socket closed.")

if __name__ == '__main__':
    error_management()