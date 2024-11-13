#
# An example of using a pipe to communicate between processes.
#

import multiprocessing


def first_process(conn):
    conn.send("Hello!")
    msg = conn.recv()
    print(f"first process received message {msg!r}")


def second_process(conn):
    msg = conn.recv()
    print(f"second process received message {msg!r}")
    conn.send("Hi!")


if __name__ == "__main__":
    # duplex=True means that the pipe is bidirectional.
    conn1, conn2 = multiprocessing.Pipe(duplex=True)

    p1 = multiprocessing.Process(target=first_process, args=(conn1,))
    p1.start()
    p2 = multiprocessing.Process(target=second_process, args=(conn2,))
    p2.start()

    p1.join()
    p2.join()
