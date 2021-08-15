from socket import socket, SOCK_DGRAM, gethostname, gethostbyname
import argparse

hostname = gethostname()
local_ip = gethostbyname(hostname)
print(local_ip)

parser = argparse.ArgumentParser()
parser.add_argument("--host", default=local_ip, required=False)
parser.add_argument("--port", type=int, default=5005, required=False)
args = parser.parse_args()

sock = socket(type = SOCK_DGRAM)
sock.bind((args.host, args.port))

while True:
  data, address = sock.recvfrom(1024)
  print(data)
sock.close()