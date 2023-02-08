class Buff:
    def __init__(self):
        self.buffer = []

    def append(self, item):
        self.buffer.append(item)

    def remove(self):
        self.buffer.pop(0)