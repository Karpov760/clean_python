import time
from contextlib import contextmanager

def long_cicle():
    sum = 0
    for i in range(20_000_000):
        sum += i

class Timer:
    """
    Таймер, принимает функции в качестве параметра функции get_time и выводит время
    """
    def __enter__(self):
        self.time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_time(self, *args):
        for arg in args:
            arg()
        print(time.time() - self.time)

class Timer2:
    """
    Таймер, печатает время выполнения инструкций блока with
    """
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(self.end - self.start)

class Timer3:
    """
    Таймер, возвращает время выполнения инструкций блока with
    """
    def __enter__(self):
        self.start = time.time()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = time.time()


@contextmanager
def timer():
    try:
        start_time = time.time()
        finish_time = 0
        yield lambda: finish_time - start_time
    finally:
        finish_time = time.time()



def main():
    with Timer() as tc:
        tc.get_time(long_cicle, long_cicle)

    with Timer2() as tc:
        long_cicle()

    with Timer3() as t3:
        long_cicle()
    print(t3())

    with timer() as t:
        long_cicle()
    print(t())

if __name__ == "__main__":
    main()