import socket
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(("", port))

print(f"Server listening on port {port}")

while True:
    datagrama, origen = s.recvfrom(1024)
    datagrama = datagrama.decode("utf8")

    if datagrama == "LOOKING FOR HELLO":
        print(f"Received discovery request from {origen[0]}")
        s.sendto(b"HELLO IMPLEMENT", origen)
    elif datagrama == "HELLO":
        print(f"Received HELLO from {origen[0]}")
        s.sendto(f"HELLO: {origen[0]}".encode("utf-8"), origen)