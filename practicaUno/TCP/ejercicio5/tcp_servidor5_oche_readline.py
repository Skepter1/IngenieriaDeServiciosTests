import socket
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 9998

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))
s.listen(5)

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    f = sd.makefile(encoding="utf8", newline="\r\n")
    print("Nuevo cliente conectado desde %s, %d" % origen)
    continuar = True
    

    

    while continuar:
        mensaje = f.readline()

        if not mensaje: 
            print("Cliente desconectado")
            sd.close()
            continuar = False
        else:
            print(f"Recibido mensaje: {repr(mensaje)}")
            
            # Odcinamy \r\n, odwracamy tekst i odsyłamy z \r\n na końcu
            linea = mensaje[:-2]
            linea = linea[::-1]
            sd.sendall((linea + "\r\n").encode("utf-8"))
            print(f"Enviada respuesta: {linea}")