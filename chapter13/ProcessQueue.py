from multiprocessing import Queue, Process
import random


def getter(name, queue):
    print('son process %s' % name)
    while True:
        try:
            value = queue.get(True, None)
            print('process getter get: %f' % value)
        except Exception:
            break


def putter(name, queue):
    print('son process %s' % name)
    for i in range(0, 10):
        value = random.random()
        queue.put(value)
        print('process putter put: %f' % value)


if __name__ == '__main__':
    queue = Queue()
    getter_process = Process(target=getter, args=('getter', queue))
    putter_process = Process(target=putter, args=('putter', queue))
    getter_process.start()
    putter_process.start()
