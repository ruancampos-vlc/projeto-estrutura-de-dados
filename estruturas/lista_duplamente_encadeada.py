from typing import Generic, Optional, TypeVar

from nos.no_duplo import NoDuplo

T = TypeVar("T")


class ListaDuplamenteEncadeada(Generic[T]):
    def __init__(self):
        self._inicio: Optional[NoDuplo[T]] = None
        self._fim: Optional[NoDuplo[T]] = None
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

        if posicao == 0:
            self.insertFirst(valor)
            return

        if posicao == self._tamanho:
            self._insertLast(valor)
            return

        atual = self._obter_no(posicao)
        anterior = atual.anterior
        novo_no = NoDuplo(valor)

        novo_no.anterior = anterior
        novo_no.proximo = atual

        anterior.proximo = novo_no
        atual.anterior = novo_no

        self._tamanho += 1

    def remove(self, valor: T) -> T:
        atual = self._inicio

        while atual is not None:
            if atual.valor == valor:
                return self._remover_no(atual)

            atual = atual.proximo

        raise ValueError("Elemento não encontrado.")

    def toArray(self) -> list[T]:
        elementos: list[T] = []
        atual = self._inicio

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def insertFirst(self, valor: T):
        novo_no = NoDuplo(valor)
        novo_no.proximo = self._inicio

        if self._inicio is None:
            self._fim = novo_no
        else:
            self._inicio.anterior = novo_no

        self._inicio = novo_no
        self._tamanho += 1

    def removeFirst(self) -> T:
        if self._inicio is None:
            raise IndexError("A lista está vazia.")

        return self._remover_no(self._inicio)

    def removeLast(self) -> T:
        if self._fim is None:
            raise IndexError("A lista está vazia.")

        return self._remover_no(self._fim)

    def _insertLast(self, valor: T):
        novo_no = NoDuplo(valor)
        novo_no.anterior = self._fim

        if self._fim is None:
            self._inicio = novo_no
        else:
            self._fim.proximo = novo_no

        self._fim = novo_no
        self._tamanho += 1

    def _remover_no(self, no: NoDuplo[T]) -> T:
        if no.anterior is None:
            self._inicio = no.proximo
        else:
            no.anterior.proximo = no.proximo

        if no.proximo is None:
            self._fim = no.anterior
        else:
            no.proximo.anterior = no.anterior

        self._tamanho -= 1
        return no.valor

    def _obter_no(self, posicao: int) -> NoDuplo[T]:
        if posicao < self._tamanho // 2:
            atual = self._inicio

            for _ in range(posicao):
                atual = atual.proximo

            return atual

        atual = self._fim

        for _ in range(self._tamanho - 1, posicao, -1):
            atual = atual.anterior

        return atual