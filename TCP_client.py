import socket

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("localhost", 5000))
    print("Conectado al servidor en localhost:5000")

    while True:
        mensaje = input("Ingresa un mensaje: ")
        cliente.send(mensaje.encode())

        if mensaje == "DESCONEXION":
            print("Cerrando conexión con el servidor.")
            cliente.close()
            break

        respuesta = cliente.recv(1024).decode()
        print(f"Respuesta del servidor: {respuesta}")

iniciar_cliente()
