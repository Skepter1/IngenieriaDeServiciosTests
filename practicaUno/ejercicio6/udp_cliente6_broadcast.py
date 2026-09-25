import socket
import sys

# Domyślnie adres ogólny broadcastu lub konkretny Twojej podsieci
ip_broadcast = sys.argv[1] if len(sys.argv) > 1 else "<broadcast>"
puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Krok 1: Wysłanie pojedynczego pakietu rozgłoszeniowego
print(f"Szukanie serwerów na {ip_broadcast}:{puerto}...")
s.sendto(b"LOOKING FOR HELLO", (ip_broadcast, puerto))

# Krok 2: Oczekiwanie na wszystkie serwery (np. przez 2 sekundy)
s.settimeout(2.0)
primer_servidor = None

while True:
    try:
        datagrama, origen = s.recvfrom(1024)
        tekst = datagrama.decode("utf-8")
        
        if tekst == "HELLO IMPLEMENT":
            print(f"Znaleziono serwer: {origen[0]}")
            # Zapamiętujemy tylko pierwszy serwer, który odpowiedział
            if primer_servidor is None:
                primer_servidor = origen
    except socket.timeout:
        # Koniec czasu - nikt więcej nie odpowiedział
        print("Koniec fazy wyszukiwania.")
        break

# Krok 3: Przetestowanie usługi na pierwszym znalezionym serwerze
if primer_servidor:
    print(f"\nTestowanie usługi na {primer_servidor[0]}...")
    s.sendto(b"HELLO", primer_servidor)
    
    # Odbieramy właściwą odpowiedź usługi
    odpowiedz, _ = s.recvfrom(1024)
    print("Otrzymano wynik:", odpowiedz.decode("utf-8"))
else:
    print("Nie znaleziono żadnego aktywnego serwera.")

s.close()