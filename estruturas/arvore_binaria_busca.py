from typing import Generic, Optional, TypeVar

from nos.no_arvore import NoArvore

T = TypeVar("T")


class ArvoreBinariaBusca(Generic[T]):
    def __init__(self):
        self._raiz: Optional[NoArvore[T]] = None
        self._tamanho = 0

    def getRoot(self) -> Optional[NoArvore[T]]:
        return self._raiz

    def isEmpty(self) -> bool:
        return self._raiz is None

    def height(self) -> int:
        return self._altura_no(self._raiz)

    def search(self, valor: T) -> Optional[NoArvore[T]]:
        atual = self._raiz

        while atual is not None:
            if valor == atual.valor:
                return atual

            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return None

    def insert(self, valor: T) -> NoArvore[T]:
        if self._raiz is None:
            self._raiz = NoArvore(valor)
            self._tamanho = 1
            return self._raiz

        atual = self._raiz

        while True:
            if valor == atual.valor:
                raise ValueError("Elementos duplicados não são permitidos.")

            if valor < atual.valor:
                if atual.esquerda is None:
                    novo_no = NoArvore(valor, atual)
                    atual.esquerda = novo_no
                    self._tamanho += 1
                    self._atualizar_alturas(atual)
                    return novo_no

                atual = atual.esquerda

            else:
                if atual.direita is None:
                    novo_no = NoArvore(valor, atual)
                    atual.direita = novo_no
                    self._tamanho += 1
                    self._atualizar_alturas(atual)
                    return novo_no

                atual = atual.direita

    def remove(self, valor: T) -> T:
        no = self.search(valor)

        if no is None:
            raise ValueError("Elemento não encontrado.")

        valor_removido = no.valor

        if no.esquerda is not None and no.direita is not None:
            sucessor = self.minimum(no.direita)
            no.valor = sucessor.valor
            no = sucessor

        filho = no.esquerda if no.esquerda is not None else no.direita
        pai = no.pai

        self._substituir_no(no, filho)
        self._tamanho -= 1
        self._atualizar_alturas(pai)

        return valor_removido

    def preOrder(self) -> list[T]:
        resultado: list[T] = []
        self._pre_ordem(self._raiz, resultado)
        return resultado

    def order(self) -> list[T]:
        resultado: list[T] = []
        self._em_ordem(self._raiz, resultado)
        return resultado

    def postOrder(self) -> list[T]:
        resultado: list[T] = []
        self._pos_ordem(self._raiz, resultado)
        return resultado

    def size(self) -> int:
        return self._tamanho

    def minimum(
        self,
        no: Optional[NoArvore[T]] = None
    ) -> NoArvore[T]:
        if self._raiz is None:
            raise IndexError("A árvore está vazia.")

        atual = self._raiz if no is None else no

        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual

    def maximum(
        self,
        no: Optional[NoArvore[T]] = None
    ) -> NoArvore[T]:
        if self._raiz is None:
            raise IndexError("A árvore está vazia.")

        atual = self._raiz if no is None else no

        while atual.direita is not None:
            atual = atual.direita

        return atual

    def _substituir_no(
        self,
        no_antigo: NoArvore[T],
        no_novo: Optional[NoArvore[T]]
    ):
        if no_antigo.pai is None:
            self._raiz = no_novo

        elif no_antigo == no_antigo.pai.esquerda:
            no_antigo.pai.esquerda = no_novo

        else:
            no_antigo.pai.direita = no_novo

        if no_novo is not None:
            no_novo.pai = no_antigo.pai

    def _altura_no(self, no: Optional[NoArvore[T]]) -> int:
        if no is None:
            return 0

        return no.altura

    def _recalcular_altura(self, no: NoArvore[T]):
        altura_esquerda = self._altura_no(no.esquerda)
        altura_direita = self._altura_no(no.direita)

        no.altura = 1 + max(altura_esquerda, altura_direita)

    def _atualizar_alturas(self, no: Optional[NoArvore[T]]):
        atual = no

        while atual is not None:
            self._recalcular_altura(atual)
            atual = atual.pai

    def _pre_ordem(
        self,
        no: Optional[NoArvore[T]],
        resultado: list[T]
    ):
        if no is None:
            return

        resultado.append(no.valor)
        self._pre_ordem(no.esquerda, resultado)
        self._pre_ordem(no.direita, resultado)

    def _em_ordem(
        self,
        no: Optional[NoArvore[T]],
        resultado: list[T]
    ):
        if no is None:
            return

        self._em_ordem(no.esquerda, resultado)
        resultado.append(no.valor)
        self._em_ordem(no.direita, resultado)

    def _pos_ordem(
        self,
        no: Optional[NoArvore[T]],
        resultado: list[T]
    ):
        if no is None:
            return

        self._pos_ordem(no.esquerda, resultado)
        self._pos_ordem(no.direita, resultado)
        resultado.append(no.valor)