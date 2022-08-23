class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self) -> int:
        return self.a + self.b

    def sub(self) -> int:
        return self.a - self.b

    def mul(self) -> int:
        return self.a * self.b

    def div(self) -> int:
        return self.a / self.b

    def mod(self) -> int:
        return self.a % self.b

    def pow(self) -> int:
        return self.a ** self.b

    def rshift(self) -> int:
        return self.a << self.b

    def lshift(self) -> int:
        return self.a >> self.b