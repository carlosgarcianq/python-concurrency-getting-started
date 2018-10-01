import threading

class FibonacciThread(threading.Thread):
    def __init__(self, num):
        super(FibonacciThread, self).__init__()
        self.num = num

    def run(self):
        fib = [0] * (self.num + 1)
        fib[0] = 0
        fib[1] = 1
        for i in range(2, len(fib)):
            fib[i] = fib[i - 1] + fib[i - 2]
        print(fib[self.num])

myFib1 = FibonacciThread(9)
myFib2 = FibonacciThread(6)

myFib1.start()
myFib2.start()

myFib1.join()
myFib2.join()

print('Done')

