import os
from multiprocessing import Pipe, Process


def send(conn):
    print(f"{os.getpid()}가 {os.getppid()}에게 데이터를 보낸다!")
    conn.send("Hello parent!")
    conn.close()


if __name__ == "__main__":
    parent, child = Pipe()
    p = Process(target=send, args=(child,))
    p.start()
    print("기존 프로세스 아이디 :", os.getpid())
    print(parent.recv())
    p.join()
