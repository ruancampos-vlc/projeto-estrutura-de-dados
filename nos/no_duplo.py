from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class NoDuplo(Generic[T]):
    def __init__(self, valor: T):
        self.valor = valor
        self.anterior: Optional["NoDuplo[T]"] = None
        self.proximo: Optional["NoDuplo[T]"] = None