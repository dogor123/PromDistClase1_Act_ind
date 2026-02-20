import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

mensaje = client.recv(1024)
print("Mensaje recibido: ", mensaje.decode())

client.close()
