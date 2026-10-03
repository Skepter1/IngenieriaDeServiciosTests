import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto_servidor = int(sys.argv[2]) if len(sys.argv) > 2 else 9997

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto_servidor))
f = s.makefile(encoding="utf8", newline="\n")

mensajes = ["HOLA", "MUNDO", "PRUEBA"]

# 1. Wysłanie wiadomości pod rząd
for m in mensajes:
    longitud  = "%d\n" % len(bytes(m, "utf8"))
    s.sendall(bytes(longitud + m, "utf8"))
    print(f"Mensaje enviado: {m}")

# 2. Odebranie odpowiedzi za pomocą recibeMensaje
for _ in range(len(mensajes)):
    longtitud = f.readline()

    longitud = int(longtitud.strip())
    mensaje = f.read(longitud)
    
    print(f"Respuesta recibida: {repr(mensaje)}")

s.close()