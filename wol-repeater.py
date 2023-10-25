import socket
import sys

def validate_magic(packet):
    if(len(packet) != 102):
        return False
    
    #Validate start of packet being ff:ff:ff:ff:ff:ff
    sum = 0
    for i in range(6):
        sum += packet[i]

    if(sum != 255*6):
        return False
    
    mac = bytearray(6)
    mac = packet[6:12]
    #Validate 16 instances of the mac address
    for i in range(15):
        if mac != packet[(i+2)*6:(i+3)*6]:
            return False
    return True


if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    broadcast_ip = sys.argv[2]
    port = 9
else:
    print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.10> <arg2:broadcast ip:192.168.1.255")
    exit(1)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enables broadcasting packets
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Bind the socket to the port
server_address = (ip, port)
server_socket.bind(server_address)

print("####### wol-relay is listening #######")
#print("wol-relay listening to:)
print("IP: %s" % ip)
print("Port: %s" % port)

while True:
    magic_packet, address = server_socket.recvfrom(4096)
    print("Server received: ", magic_packet, "\n")
    print("Server received len: ", len(magic_packet), "\n")

    if(validate_magic(magic_packet)):
        print("validated")
        server_socket.sendto(magic_packet, (broadcast_ip, port))
