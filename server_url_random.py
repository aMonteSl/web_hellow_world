#!/usr/bin/python3

import socket
import random

import random

# Construye la respuesta HTTP con la imagen
RESPONSE = "HTTP/1.1 200 OK\r\n\r\n" \
           + "<html><body><h1>Hello World</h1>" \
           + "<a href='" + str(random.randint(0, 10000)) + "'>Dame otra</a>" \
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

        # Construye la respuesta HTTP con la imagen
        respuesta = "HTTP/1.1 200 OK\r\n\r\n" \
                + "<html><body><h1>Hello World</h1>" \
                + "<a href='" + str(random.randint(0, 10000)) + "'>Dame otra</a>" \
                + "</body></html>" \
                + "\r\n"

        connectionSocket.send(respuesta.encode("utf-8"))
        connectionSocket.close()