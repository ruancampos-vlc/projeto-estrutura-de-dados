from typing import Generic, Optional, TypeVar

from nos.no import No

T = TypeVar("T")


class ListaEncadeada(Generic[T]):
    def __init__(self):
        self._inicio: Optional[No[T]] = None
        self._tamanho = 0

    def isEmpty(self) -> bool:
        return self._tamanho == 0

    def size(self) -> int:
        return self._tamanho

    def search(self, valor: T) -> int:
        atual = self._inicio
        posicao = 0

        while atual is not None:
            if atual.valor == valor:
                return posicao

            atual = atual.proximo
            posicao += 1

        return -1

    def insert(self, valor: T, posicao: Optional[int] = None):
        if posicao is None:
            posicao = self._tamanho

        if posicao < 0 or posicao > self._tamanho:
            raise IndexError("Posição inválida.")

        novo_no = No(valor)

        if posicao == 0:
            novo_no.proximo = self._inicio
            self._inicio = novo_no
        else:
            anterior = self._obter_no(posicao - 1)
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no

        self._tamanho += 1

    def remove(self, valor: T) -> T:
        if self.isEmpty():
            raise IndexError("A lista está vazia.")

        atual = self._inicio
        anterior: Optional[No[T]] = None

        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self._inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                self._tamanho -= 1
                return atual.valor

            anterior = atual
            atual = atual.proximo

        raise ValueError("Elemento não encontrado.")

    def toArray(self) -> list[T]:
        elementos: list[T] = []
        atual = self._inicio

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def _obter_no(self, posicao: int) -> No[T]:
        atual = self._inicio

        for _ in range(posicao):
            atual = atual.proximo

        return atual