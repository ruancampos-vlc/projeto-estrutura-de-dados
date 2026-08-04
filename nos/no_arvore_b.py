from typing import Generic, TypeVar

T = TypeVar("T")


class NoArvoreB(Generic[T]):
    def __init__(self, folha: bool = True):
        self.folha = folha
        self.chaves: list[T] = []
        self.filhos: list["NoArvoreB[T]"] = []