class Stack:
    def __init__(self):
        self.lt = []

    def is_empty(self):
        return self.lt == []

    def push(self, elements):
        self.lt.append(elements)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.lt.pop()

    def peep(self):
        n = len(self.lt)
        return self.lt[n-1]

    def search(self, elements):
        if self.is_empty():
            return -1
        else:
            try:
                n = self.lt.index(elements)
                return len(self.lt)-n
            except ValueError:
                return -2

    def display(self):
        return self.lt
