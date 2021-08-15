from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

sock = socket(AF_INET, SOCK_DGRAM)

while True:
  data = input("Digite uma mensagem:")
  print(data)
  print(sock.sendto(data.encode(), (SERVER_IP, SERVER_PORT)))