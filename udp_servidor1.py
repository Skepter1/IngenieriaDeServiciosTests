import socket
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))

print(f"Serwer nasłuchuje na porcie {port}")

while True:
    datagrama, origen = s.recvfrom(1024)
    print("Se ha recibido un datagrama desde", origen)
    print("Contiene lo siguiente:")
    print(datagrama.decode("utf-8"))