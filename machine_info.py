import socket
import netifaces

def get_machine_info():
    host_name = socket.gethostname() # retrieve host name 
    ip_address = socket.gethostbyname(host_name) # obtain ip address

    print("Host name: ", host_name)
    print("IP address: ", ip_address)

    interfaces = netifaces.interfaces() # get interfaces

    print("Network Interfaces: ")

    for interface in interfaces:
        print(interface)

if __name__ == '__main__':
    try:
        get_machine_info()
    except socket.error as e:
        print(f"Error occured: {e}")


