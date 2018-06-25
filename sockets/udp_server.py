from socket import *

if __name__ == "__main__":
	server_port = 12000
	server_socket = socket(AF_INET, SOCK_DGRAM)
	# Bind IP + Port
	server_socket.bind(("", server_port))
	
	print "Server is ready to receive data."

	while 1: 
		msg, client_addr = server_socket.recvfrom(2048)
		print "[" + str(client_addr) + "]: " + msg
		new_msg = msg.upper()
		server_socket.sendto(new_msg, client_addr)
