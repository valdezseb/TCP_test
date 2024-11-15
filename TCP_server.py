import socket

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("localhost", 5000))
    servidor.listen(5)  # Permite hasta 5 conexiones en cola
    print("Servidor TCP en espera de conexiones en localhost:5000...")

    while True:
        cliente_socket, direccion = servidor.accept()
        print(f"Conexión aceptada de {direccion}")

        while True:
            mensaje = cliente_socket.recv(1024).decode()
            if not mensaje:
                break

            print(f"Mensaje recibido: {mensaje}")

            if mensaje == "DESCONEXION":
                print("Cerrando conexión con el cliente.")
                cliente_socket.close()
                break

            respuesta = mensaje.upper()
            cliente_socket.send(respuesta.encode())
            print(f"Respuesta enviada: {respuesta}")

iniciar_servidor()
