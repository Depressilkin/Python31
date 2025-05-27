import socket

HOST = '127.0.0.1'  # IP-адрес сервера
PORT = 12345        # порт сервера

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        welcome = s.recv(1024).decode()
        print(welcome)

        while True:
            message = input("Ваше сообщение: ")
            s.sendall((message + "\n").encode())

            if message == "/exit":
                break

            data = s.recv(1024).decode()
            print("Ответ от собеседника:", data)

if __name__ == "__main__":
    main()