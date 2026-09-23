import socket
import sys

# Pobranie IP i portu z argumentów wiersza poleceń lub użycie domyślnych
ip_servidor = sys.argv[1] if len(sys.argv) > 1 else "localhost"
puerto_servidor = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    texto = input("Wpisz wiadomość (lub 'END' aby zakończyć): ")
    
    if texto == "END":
        break
        
    s.sendto(texto.encode("utf-8"), (ip_servidor, puerto_servidor))

s.close()