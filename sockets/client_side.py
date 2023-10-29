from socket import socket as Socket, SHUT_RDWR


def main(host: str, port: int, message: str):
    """"""

    address: tuple[str, int] = (host, port)

    time_out: int = 60
    buffer: int = 1024

    socket: Socket = Socket()
    # self.__address = address

    socket.settimeout(time_out)
    socket.connect(address)

    flag: bool = False

    while True:
        message_send: str = ""
        if message == "":
            message_send = input("> ")
        else:
            message_send = message
            flag = True

        if message_send == ".quit":
            break

        # 送信
        socket.send(message_send.encode("utf-8"))

        # 受信
        message_recv: str = socket.recv(buffer).decode("utf-8")
        print(message_recv)

        if flag:
            break

    socket.shutdown(SHUT_RDWR)
    socket.close()


if __name__ == "__main__":
    message: str = ""
    main(host="127.0.0.1", port=8890, message=message)
