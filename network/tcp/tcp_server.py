"""
Simple tcp server, reverses the packet.

Alan Marchiori
"""
import socket
import threading

TCP_IP = "" # empty string is the default interface, all IPs
TCP_PORT = 3333

print ("TCP target IP:", TCP_IP)
print ("TCP target port:", TCP_PORT)

def handle_client(conn, addr):
    while(True):
        buf = conn.recv(2048)
        if len(buf) == 0:
            break
        print(f"Recv from {addr} [{len(buf)}]: {buf.decode()}")
        
        print(f"Send to   {addr} [{len(buf)}]: {buf[::-1].decode()}")
        conn.send(buf[::-1])
    print( f"Disconnect from client {addr}")
    conn.close()

with socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) as sock: # TCP

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen()
    while (True):

        (conn, addr) = sock.accept() 
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, 
            args=(conn, addr), 
            daemon=True).start()
        


    


    
