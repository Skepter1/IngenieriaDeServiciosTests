import socket
import sys

ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto_servidor = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n = 1

while True:
    texto = input("Wpisz wiadomość (lub 'END' aby zakończyć): ")
    
    if texto == "END":
        break
    
    s.sendto(f"{n}: {texto}".encode("utf-8"), (ip_servidor, puerto_servidor))
    n += 1
    
    s.settimeout(0.1)
    try:
        datagrama, origen = s.recvfrom(1024)
        datagrama = datagrama.decode("utf8")
        if datagrama=="OK":
            print("Recibida confirmación")
        else:
            print("Recibido datagrama no esperado")
    except socket.timeout:
        print("ERROR. El datagrama de confirmación no llega")
    except:
        raise

s.close()