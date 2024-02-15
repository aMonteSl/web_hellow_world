#!/usr/bin/python3

import socket

# Construye la respuesta HTTP con la imagen
RESPONSE = "HTTP/1.1 200 OK\r\n\r\n" \
           + "<html><body><h1>Hello World</h1>" \
           + "<img src= 'https://upload.wikimedia.org/wikipedia/commons/4/4d/Logo_urjc.png' />" \
           + "</body></html>" \
           + "\r\n"

if __name__ == "__main__":
    # AF_INET = IPv4, SOCK_STREAM = TCP
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Habilitar reutilización de direcciones
    mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    mySocket.bind(("", 1234))
    
    # Cola máxima de 5 conexiones TCP
    mySocket.listen(5)

    while True:
        print("Esperando alguna conexión...")
        connectionSocket, addr = mySocket.accept()
        print("Conexión recibida de: " + str(addr))
        recibido = connectionSocket.recv(2048)
        print(recibido)

        connectionSocket.send(RESPONSE.encode("utf-8"))
        connectionSocket.close()
