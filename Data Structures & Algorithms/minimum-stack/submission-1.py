class MinStack:

    def __init__(self):
        self.main = []
        self.minSt = []

    def push(self, val: int) -> None:
        self.main.append(val)
        if self.minSt:
            self.minSt.append(min(val, self.minSt[-1]))
        else:
            self.minSt.append(val)

    def pop(self) -> None:
        self.main.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
