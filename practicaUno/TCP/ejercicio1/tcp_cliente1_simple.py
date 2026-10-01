import sys
import socket

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto_servidor = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_servidor, puerto_servidor))

    #texto = input("Escribe tu mensaje o pulsa 'Finalizar' para terminar.")

    # if texto == "END":
    #         break

texto = f"ABCDE"
for i in range(1, 6):
    s.send(texto.encode("utf-8"))
    print(f"Mensaje enviado: {texto}")
s.send("FINAL".encode("utf-8"))
print(f"Mensaje enviado: FINAL")

s.close()