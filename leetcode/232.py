class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def pop(self) -> int:
        if self.b:
            return self.b.pop()
        if self.a:
            self.b = list(self.a[::-1])
            self.a = list()
            return self.b.pop()
        return -1
        
    def peek(self) -> int:
        if self.b:
            return self.b[-1]
        elif self.a:
            return self.a[0]
        return -1
        
    def empty(self) -> bool:
        return not self.a and not self.b
        

q = MyQueue()
print(q.push(1))
print(q.push(2))
print(q.pop())
print(q.pop())
print(q.push(3))
print(q.push(2))
print(q.push(1))
print(q.pop())
print(q.pop())
print(q.empty())
