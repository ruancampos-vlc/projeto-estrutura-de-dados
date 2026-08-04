from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Fila(Generic[T]):
    def __init__(self, capacidade: int):
        self.create(capacidade)

    def create(self, capacidade: int):
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")

        self._capacidade = capacidade
        self._elementos: list[Optional[T]] = []

        for _ in range(capacidade):
            self._elementos.append(None)

        self._inicio = 0
        self._fim = 0
        self._quantidade = 0

    def enqueue(self, elemento: T):
        if self.isFull():
            raise OverflowError("A fila está cheia.")

        self._elementos[self._fim] = elemento
        self._fim = (self._fim + 1) % self._capacidade
        self._quantidade += 1

    def dequeue(self) -> T:
        if self.isEmpty():
            raise IndexError("A fila está vazia.")

        elemento = self._elementos[self._inicio]
        self._elementos[self._inicio] = None
        self._inicio = (self._inicio + 1) % self._capacidade
        self._quantidade -= 1

        return elemento

    def head(self) -> T:
        if self.isEmpty():
            raise IndexError("A fila está vazia.")

        return self._elementos[self._inicio]

    def isEmpty(self) -> bool:
        return self._quantidade == 0

    def isFull(self) -> bool:
        return self._quantidade == self._capacidade

    def toArray(self) -> list[T]:
        resultado: list[T] = []

        for indice in range(self._quantidade):
            posicao = (self._inicio + indice) % self._capacidade
            elemento = self._elementos[posicao]

            if elemento is not None:
                resultado.append(elemento)

        return resultado