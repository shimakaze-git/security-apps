from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM, SHUT_RDWR


def main(host: str, port: int):

    address: tuple[str, int] = (host, port)

    time_out: int = 60
    buffer: int = 1024

    # ソケットの作成
    socket: Socket = Socket(AF_INET, SOCK_STREAM, 0)
    socket.settimeout(time_out)

    # ソケットをローカルのアドレス（ソケットファイルやIP+ポート）にバインド
    socket.bind(address)

    # ソケットに接続を待ち受けるように命令
    socket.listen(1)

    print("Server [started] :", address)

    # 外部からの接続に対して新しいソケットを作成
    conn: Socket
    conn, _ = socket.accept()

    while True:
        try:
            # データの受信を行う
            message: bytes = conn.recv(buffer)

            message_recv: str = message.decode("utf-8")
            message_resp: str = f"response: ({message_recv})"
            print("[message_resp]", message_resp)

            # データの送信を行う
            conn.send(message_resp.encode("utf-8"))
        except ConnectionResetError:
            break
        except BrokenPipeError:
            break

    # ソケットをクローズし、ファイルディスクリプタも削除する。
    socket.shutdown(SHUT_RDWR)
    socket.close()


if __name__ == "__main__":
    host: str = "127.0.0.1"
    port: int = 8890

    main(host, port)
