from socket import *

if __name__ == "__main__":
	server_port = 12000
	server_socket = socket(AF_INET, SOCK_STREAM)
	# Bind IP + Port
	server_socket.bind(("", server_port))

	# Argument: Max number of queued connections
	server_socket.listen(1)
	conn_socket, client_addr = server_socket.accept()
	while 1:
		# Create a new socket after 3-way handshake
		
		rcv_msg = conn_socket.recv(2048)
		rcv_msg = rcv_msg.decode()
		print("[" + str(client_addr) + "]: " + rcv_msg)

		if(rcv_msg == "close"):
			conn_socket.close()
			break
		
		new_msg = rcv_msg.upper()
		conn_socket.send(new_msg.encode())

		# Close connection, so a new user may connect
	conn_socket.close()
