import time

class Buff:
    def __init__(self):
        self.buffer = []

    def append(self, item):
        while (len(self.buffer) > 2):
                time.sleep(0)
        self.buffer.append(item)

    def remove(self):
        self.buffer.pop(0)