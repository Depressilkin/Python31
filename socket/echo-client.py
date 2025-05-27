import socket

HOST = "127.0.0.1"  # ип-адресс локально
PORT = 65432  # порт от 1 до 65535  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Конец {data}")
