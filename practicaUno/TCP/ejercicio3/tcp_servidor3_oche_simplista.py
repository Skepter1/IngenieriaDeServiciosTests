import socket
import sys

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
        mensaje = sd.recv(80)

        if not mensaje: 
            print("Conexión cerrada de forma inesperada por el cliente")
            
            sd.close()
            continuar = False
        else:
            mensaje = mensaje.decode("utf-8")
            print(f"Recibido mensaje: {repr(mensaje)}")
            
            linea = mensaje[:-2]
            linea = linea[::-1]
            
            sd.sendall(f"{linea}\r\n".encode("utf-8"))
            print(f"Respuesta enviada: {linea}")
                    