from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class No(Generic[T]):
    def __init__(self, valor: T):
        self.valor = valor
        self.proximo: Optional["No[T]"] = None