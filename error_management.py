import socket

SEND_BUFF_SIZE = 4096
RECV_BUFF_SIZE = 2048

def socket_settings():
    print("Socket Settings")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get and print default buffer size
    send_buf_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Send buffer size: ", send_buf_size)
    recv_buf_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Received buffer size: ", recv_buf_size)

    # modify buffer sizes
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)

    send_buf_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Modified send buffer size after: ", send_buf_size)
    recv_buf_size = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Modified recevied buffer size: ", recv_buf_size)

    # switch non-blocking mode
    sock.setblocking(False)
    print("Non blocking mode")
    sock.settimeout(3)
    print("Socket timeout: ", sock.gettimeout(), " seconds")

def error_management_test():
    print("Error Management Test")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        # connect to a dead ip to trigger an error
        sock.connect(('111.111.111.111', 80))
    except socket.timeout:
        # catch timeout error
        print("Connection timeout")
    except socket.error as e:
        # catch general socket errors
        print(f"{e} Error")
    finally:
        sock.close()
        print("Socket closed.")

if __name__ == '__main__':
    socket_settings()
    error_management_test()