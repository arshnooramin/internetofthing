"""
Simple udp server, reverses the packet.

Alan Marchiori
"""
import socket

#UDP_IP = "0.0.0.0"
UDP_IP = "" # empty string is the default interface, all IPs
UDP_PORT = 8888

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)

i = 0

with socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) as sock: # UDP

    sock.bind((UDP_IP, UDP_PORT))
    
    while (True):
        buf, addr = sock.recvfrom(2048)

        print(f"Recv from {addr} [{len(buf)}]: {buf.decode()}")
        
        print(f"Send to   {addr} [{len(buf)}]: {buf[::-1].decode()}")
        sock.sendto(buf[::-1], addr)


    


    
