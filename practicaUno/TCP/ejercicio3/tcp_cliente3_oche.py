import sys
import socket

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto_servidor = int(sys.argv[2]) if len(sys.argv) > 2 else 9998

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto_servidor))

texto = f"HOLA"
fin = f"\r\n"
s.send((texto + fin).encode("utf-8"))
print(f"Mensaje enviado: {texto}")

datos = s.recv(1024)
datos = datos.decode("utf-8")

print(f"Respuesta recibida: {datos}")

s.close()