from typing import Generic, TypeVar

T = TypeVar("T")


class Pilha(Generic[T]):
    def __init__(self, capacidade: int):
        self.create(capacidade)

    def create(self, capacidade: int):
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")

        self._capacidade = capacidade
        self._elementos: list[T] = []

    def push(self, elemento: T):
        if self.isFull():
            raise OverflowError("A pilha está cheia.")

        self._elementos.append(elemento)

    def pop(self) -> T:
        if self.isEmpty():
            raise IndexError("A pilha está vazia.")

        return self._elementos.pop()

    def top(self) -> T:
        if self.isEmpty():
            raise IndexError("A pilha está vazia.")

        return self._elementos[-1]

    def isEmpty(self) -> bool:
        return len(self._elementos) == 0

    def isFull(self) -> bool:
        return len(self._elementos) == self._capacidade

    def toArray(self) -> list[T]:
        return self._elementos.copy()