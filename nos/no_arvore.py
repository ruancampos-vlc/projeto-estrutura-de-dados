from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class NoArvore(Generic[T]):
    def __init__(self, valor: T, pai: Optional["NoArvore[T]"] = None):
        self.valor = valor
        self.esquerda: Optional["NoArvore[T]"] = None
        self.direita: Optional["NoArvore[T]"] = None
        self.pai = pai
        self.altura = 1
        