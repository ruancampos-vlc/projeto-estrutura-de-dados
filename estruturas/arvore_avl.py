from typing import Optional, TypeVar

from estruturas.arvore_binaria_busca import ArvoreBinariaBusca
from nos.no_arvore import NoArvore

T = TypeVar("T")


class ArvoreAVL(ArvoreBinariaBusca[T]):
    def insert(self, valor: T) -> NoArvore[T]:
        no_inserido = super().insert(valor)
        self.rebalance_up(no_inserido)

        return no_inserido

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

        if pai is not None:
            self.rebalance_up(pai)

        elif filho is not None:
            self.rebalance_up(filho)

        return valor_removido

    def calculate_balance(
        self,
        no: Optional[NoArvore[T]]
    ) -> int:
        if no is None:
            return 0

        altura_esquerda = self._altura_no(no.esquerda)
        altura_direita = self._altura_no(no.direita)

        return altura_esquerda - altura_direita

    def rebalance(self, no: NoArvore[T]) -> NoArvore[T]:
        fator = self.calculate_balance(no)

        if fator > 1:
            if self.calculate_balance(no.esquerda) < 0:
                self.left_rotation(no.esquerda)

            return self.right_rotation(no)

        if fator < -1:
            if self.calculate_balance(no.direita) > 0:
                self.right_rotation(no.direita)

            return self.left_rotation(no)

        return no

    def rebalance_up(self, no: Optional[NoArvore[T]]):
        atual = no

        while atual is not None:
            self._recalcular_altura(atual)
            nova_raiz = self.rebalance(atual)
            atual = nova_raiz.pai

    def left_rotation(self, no: NoArvore[T]) -> NoArvore[T]:
        nova_raiz = no.direita

        if nova_raiz is None:
            return no

        subarvore_transferida = nova_raiz.esquerda
        pai_original = no.pai

        nova_raiz.pai = pai_original

        if pai_original is None:
            self._raiz = nova_raiz

        elif no == pai_original.esquerda:
            pai_original.esquerda = nova_raiz

        else:
            pai_original.direita = nova_raiz

        nova_raiz.esquerda = no
        no.pai = nova_raiz
        no.direita = subarvore_transferida

        if subarvore_transferida is not None:
            subarvore_transferida.pai = no

        self._recalcular_altura(no)
        self._recalcular_altura(nova_raiz)

        return nova_raiz

    def right_rotation(self, no: NoArvore[T]) -> NoArvore[T]:
        nova_raiz = no.esquerda

        if nova_raiz is None:
            return no

        subarvore_transferida = nova_raiz.direita
        pai_original = no.pai

        nova_raiz.pai = pai_original

        if pai_original is None:
            self._raiz = nova_raiz

        elif no == pai_original.esquerda:
            pai_original.esquerda = nova_raiz

        else:
            pai_original.direita = nova_raiz

        nova_raiz.direita = no
        no.pai = nova_raiz
        no.esquerda = subarvore_transferida

        if subarvore_transferida is not None:
            subarvore_transferida.pai = no

        self._recalcular_altura(no)
        self._recalcular_altura(nova_raiz)

        return nova_raiz