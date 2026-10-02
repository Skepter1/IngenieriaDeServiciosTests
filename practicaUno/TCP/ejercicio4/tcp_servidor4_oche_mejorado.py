import socket
import sys

def recibeMensaje(sd):
    mensaje = []
    while True:
        trozo = sd.recv(1)
        if not trozo:
            # Rozłączenie klienta w trakcie odczytu
            return b""
        mensaje.append(trozo)
        # Sprawdzamy czy ostatnie 2 elementy to \r i \n
        if len(mensaje) >= 2 and mensaje[-2:] == [b"\r", b"\n"]:
            break
    return b"".join(mensaje)

port = int(sys.argv[1]) if len(sys.argv) > 1 else 9998

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))
s.listen(5)

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    print("Nuevo cliente conectado desde %s, %d" % origen)
    continuar = True
    
    while continuar:
        mensaje = recibeMensaje(sd)

        if not mensaje: 
            print("Cliente desconectado")
            sd.close()
            continuar = False
        else:
            texto = mensaje.decode("utf-8")
            print(f"Recibido mensaje: {repr(texto)}")
            
            # Odcinamy \r\n, odwracamy tekst i odsyłamy z \r\n na końcu
            linea = texto[:-2]
            linea = linea[::-1]
            sd.sendall((linea + "\r\n").encode("utf-8"))
            print(f"Enviada respuesta: {linea}")