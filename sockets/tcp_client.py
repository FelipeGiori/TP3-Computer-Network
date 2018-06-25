from socket import *

if __name__ == "__main__":
	# AF_INET ~ IPv4
	# STREAM ~ TCP
	server_name = "localhost"
	server_port = 12000
	client_socket = socket(AF_INET, SOCK_STREAM)
	
	# 3-way handshake
	# Src IP will be attached by O.S
	# Src port can be random
	# Start 3-way handshake
	client_socket.connect((server_name, server_port))
	while 1:
		msg = input("Input message: ")

		client_socket.send(msg.encode())
		rcv_msg = client_socket.recv(2048)

		print("From server: " + rcv_msg.decode())

	client_socket.close()


	
