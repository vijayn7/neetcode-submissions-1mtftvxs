class MinStack:
    

    def __init__(self):
        self.st = []
        self.stMin = []

    def push(self, val: int) -> None:
        self.st.append(val)
        self.stMin.append(min(val, self.stMin[-1] if self.stMin else val))

    def pop(self) -> None:
        self.st.pop()
        self.stMin.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.stMin[-1]
