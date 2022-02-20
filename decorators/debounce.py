
import time


class Debounce(object):
    def __init__(self, seconds:int) -> None:
        self.seconds = seconds
        self.lastTimeCalled=None

    def __call__(self, f):
        def wrapped(*args, **kwargs):

            now = time.time()

            if self.lastTimeCalled is not None:
                delta = now - self.lastTimeCalled

                if delta >= self.seconds:
                    self.lastTimeCalled = now

                    f(*args, **kwargs)
            else:
                self.lastTimeCalled = now
                f(*args, **kwargs)

        return wrapped