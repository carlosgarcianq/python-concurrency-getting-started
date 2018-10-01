import threading

def do_some_work(value):
    print('doing some work in thread')
    print('echo: {}'.format(value))

val = "text"
t = threading.Thread(target=do_some_work, args=(val,))
print('Name: {}'.format(t.name))
t.start()
t.join()