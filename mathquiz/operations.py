from abc import ABC, abstractmethod

class Operation(ABC):
    symbol: str

    @abstractmethod
    def apply(self, a: float, b: float) -> float:
        pass

class Add(Operation):
    symbol = '+'
    def apply(self, a, b): return a + b

class Subtract(Operation):
    symbol = '-'
    def apply(self, a, b): return a - b

class Multiply(Operation):
    symbol = '*'
    def apply(self, a, b): return a * b

class Divide(Operation):
    symbol = '/'
    def apply(self, a, b): return a / b if b != 0 else float('inf')

OPERATIONS = {
    '+': Add(),
    '-': Subtract(),
    '*': Multiply(),
    '/': Divide(),
}