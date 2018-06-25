from socket import *

if __name__ == "__main__":
	# Name will be translated by DNS
	# AF_INET ~ IPv4
        # DGRAM ~ UDP
	server_name = "localhost"
	server_port = 12000
	client_socket = socket(AF_INET, SOCK_DGRAM)
	
	msg = raw_input("Input lowercase sentence: ")
	
	# Src IP addr will be attached to the packet by O.S
	# Src port can be random. Guess why?
	client_socket.sendto(msg, (server_name, server_port))

	# 2048 is buffer size
	# Connectionless; no src port
	rcv_msg, server_addr = client_socket.recvfrom(2048)
	print "[" + str(server_addr) + "]: " + rcv_msg

	# Closing socket
	client_socket.close()
