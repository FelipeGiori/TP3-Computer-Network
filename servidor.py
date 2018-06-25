from socket import *
from threading import Thread
from User import User
import sys


def on_client_connected(conn_socket, users):
    response = True

    while(response != False):
        response = receive_message(conn_socket, users)
        if(response != False):   
            conn_socket.send(response.encode())


def receive_message(conn_socket, users):
    rcv_msg = conn_socket.recv(2048)
    rcv_msg = rcv_msg.decode().split(" ")
    response = False

    if(rcv_msg[0] == 'N'):
        # Register user
        response = users.register_user(rcv_msg[1], rcv_msg[2])
    elif(rcv_msg[0] == 'S'):
        # Store a file content
        response = users.store_message(rcv_msg)
    elif(rcv_msg[0] == 'R'):
        # Return a file content
        response = users.retrieve_message(rcv_msg)
    elif(rcv_msg[0] == 'L'):
        # Return filenames
        response = users.retrieve_filenames(rcv_msg[1], rcv_msg[2])

    return response


def main():
    users = User() # Tabela de usuários

    # Connection Setup
    server_port = int(sys.argv[1])
    server_socket = socket(AF_INET6, SOCK_STREAM)
    server_socket.bind(("", server_port))
    server_socket.listen(1)

    # Accepting multiple connections
    while True:
        conn_socket, __ = server_socket.accept()
        t = Thread(target = on_client_connected, args =(conn_socket, users))
        t.start()


if __name__ == "__main__":
    main()