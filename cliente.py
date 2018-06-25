from socket import *
import sys

def connection_setup(server_name, server_port):
    # Verifica se o endereço é IPv4. Se o endereço não for IPv4, ele tenta se conectar com IPv6.
    try:
        inet_aton(server_name)
        client_socket = socket(AF_INET, SOCK_STREAM)
    except:
        client_socket = socket(AF_INET6, SOCK_STREAM)
    
    client_socket.connect((server_name, server_port))
    return client_socket


def main():
    server_name = sys.argv[1]
    server_port = int(sys.argv[2])
    client_socket = connection_setup(server_name, server_port)

    while True:
        try:
            msg = input()
        except EOFError:
            break
            
        client_socket.send(msg.encode())
        rcv_msg = client_socket.recv(2048)
        print(rcv_msg.decode())


if __name__ == "__main__":
    main()