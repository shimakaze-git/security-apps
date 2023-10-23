import socket

target_host: str = "www.google.com"
target_host = "zenn.dev"
target_port: int = 80

# create socket object
client: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect Server
client.connect((target_host, target_port))

# Send Data
reqesut_message: str = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(reqesut_message.encode("utf-8"))

# Recv Data
response: bytes = client.recv(4096)
