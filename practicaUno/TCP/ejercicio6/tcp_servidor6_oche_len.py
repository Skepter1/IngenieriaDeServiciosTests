import socket
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))
s.listen(5)

while True:
    print("Esperando un cliente")
    sd, origen = s.accept()
    f = sd.makefile(encoding="utf8", newline="\n")
    print("Nuevo cliente conectado desde %s, %d" % origen)
    continuar = True

    while continuar:
        longtitud = f.readline()
        

        if not longtitud: 
            print("Cliente desconectado")
            sd.close()
            continuar = False
        else:
            longitud = int(longtitud.strip())
            mensaje = f.read(longitud)
            
            print(f"Recibido mensaje: {repr(mensaje)}")
            
            # Odcinamy \n, odwracamy tekst i odsyłamy z \n na końcu
            linea = mensaje[::-1]
            longitud_resp  = "%d\n" % len(bytes(linea, "utf8"))
            sd.sendall(bytes(longitud_resp + linea, "utf8"))
            print(f"Enviada respuesta: {linea}")