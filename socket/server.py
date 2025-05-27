# servak
#.socket() создадите объект сокета с указанием типа сокета
#.bind() применяется для привязки сокета к конкретному сетевому интерфейсу и номеру порта:
#.listen() У метода .listen() есть параметр backlog. Он указывает число непринятых подключений, которые система разрешит до отклонения новых подключений.
#.accept() Чтобы принять или завершить такое подключение, на сервере вызывается
#.connect() подключение клиента
#.send() отправка
#.recv() получение ответа


import socket

HOST = '0.0.0.0'  # слушает все IP-адреса
PORT = 12345      # порт сервера

def handle_client(conn, addr):
    print(f"Клиент подключился: {addr}")
    conn.sendall("Добро пожаловать! Введите сообщение или /exit для завершения.\n".encode())

    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                break
            if data == "/exit":
                conn.sendall("Беседа завершена. До свидания!\n".encode())
                break
            print(f"Сообщение от {addr}: {data}")
            response = input("Введите ответ: ")
            conn.sendall((response + "\n").encode())
        except ConnectionResetError:
            print(f"Клиент {addr} отключился.")
            break

    conn.close()
    print(f"Соединение с {addr} закрыто.")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Сервер запущен и слушает порт {PORT}...")

        while True:
            conn, addr = s.accept()
            handle_client(conn, addr)
            print("Ожидание следующего клиента...")

if __name__ == "__main__":
    main()

#import socket
#import threading
#
#HOST = '0.0.0.0'  # слушает все IP-адреса
#PORT = 12345      # порт сервера
#
#def handle_client(conn, addr):
#    print(f"[+] Клиент подключился: {addr}")
#    try:
#        conn.sendall("Добро пожаловать! Введите сообщение или /exit для завершения.\n".encode())
#
#        while True:
#            data = conn.recv(1024).decode().strip()
#            if not data:
#                break
#            if data == "/exit":
#                conn.sendall("Беседа завершена. До свидания!\n".encode())
#                break
#            print(f"Сообщение от {addr}: {data}")
#            response = input(f"Введите ответ для {addr}: ")
#            conn.sendall((response + "\n").encode())
#    except ConnectionResetError:
#        print(f"[!] Клиент {addr} отключился внезапно.")
#    finally:
#        conn.close()
#        print(f"[+] Соединение с {addr} закрыто.")
#
#def main():
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#        s.bind((HOST, PORT))
#        s.listen()
#        print(f"Сервер запущен и слушает порт {PORT}...")
#
#        while True:
#            conn, addr = s.accept()
#            # запускаем поток для обслуживания клиента
#            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
#
#if __name__ == "__main__":
#    main()