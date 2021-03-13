from socket import socket, SOCK_DGRAM
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("port")
args = parser.parse_args()

sock = socket(type = SOCK_DGRAM)
sock.bind((args.host, args.port))

while True:
  data, address = sock.recvfrom(1024)
  print(data)
sock.close()