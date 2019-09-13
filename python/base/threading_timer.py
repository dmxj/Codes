# -*- coding: utf-8 -* -
import threading
import time

'''
使用子线程定时执行
'''

class Timer(threading.Thread):
    """Call a function after a specified number of seconds:

            t = Timer(30.0, f, args=None, kwargs=None)
            t.start()
            t.cancel()     # stop the timer's action if it's still waiting

    """

    def __init__(self, delay, interval, function, args=None, kwargs=None):
        threading.Thread.__init__(self)
        self.delay = delay
        self.interval = interval
        self.function = function
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self.finished = threading.Event()

    def cancel(self):
        """Stop the timer if it hasn't finished yet."""
        self.finished.set()

    def run(self):
        self.finished.wait(self.delay)
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            time.sleep(self.interval)
        self.finished.set()


if __name__ == "__main__":
    def hello_word():
        print("hello world, now time is:", time.time())

    my_timer = Timer(0, 1, hello_word)
    my_timer.start()
    print("timer is start...")
    time.sleep(10)
    print("all end")
    my_timer.cancel()
