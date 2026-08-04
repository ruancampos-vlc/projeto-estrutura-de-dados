from typing import Generic, Optional, TypeVar

from nos.no_arvore_b import NoArvoreB

T = TypeVar("T")


class ArvoreB(Generic[T]):
    def __init__(self, grau_minimo: int = 2):
        if grau_minimo < 2:
            raise ValueError(
                "O grau mínimo deve ser maior ou igual a 2."
            )

        self._grau_minimo = grau_minimo
        self._raiz = NoArvoreB[T]()
        self._tamanho = 0

    def insert(self, chave: T):
        if self.search(chave):
            raise ValueError(
                "Elementos duplicados não são permitidos."
            )

        raiz = self._raiz
        limite = (2 * self._grau_minimo) - 1

        if len(raiz.chaves) == limite:
            nova_raiz = NoArvoreB[T](folha=False)
            nova_raiz.filhos.append(raiz)

            self._raiz = nova_raiz

            self.split(nova_raiz, 0)
            self._inserir_nao_cheio(nova_raiz, chave)

        else:
            self._inserir_nao_cheio(raiz, chave)

        self._tamanho += 1

    def search(
        self,
        chave: T,
        no: Optional[NoArvoreB[T]] = None
    ) -> bool:
        atual = self._raiz if no is None else no
        indice = 0

        while (
            indice < len(atual.chaves)
            and chave > atual.chaves[indice]
        ):
            indice += 1

        if (
            indice < len(atual.chaves)
            and chave == atual.chaves[indice]
        ):
            return True

        if atual.folha:
            return False

        return self.search(chave, atual.filhos[indice])

    def split(
        self,
        pai: NoArvoreB[T],
        indice_filho: int
    ):
        grau = self._grau_minimo
        filho_cheio = pai.filhos[indice_filho]
        novo_filho = NoArvoreB[T](filho_cheio.folha)

        chave_mediana = filho_cheio.chaves[grau - 1]

        novo_filho.chaves = filho_cheio.chaves[grau:]
        filho_cheio.chaves = filho_cheio.chaves[:grau - 1]

        if not filho_cheio.folha:
            novo_filho.filhos = filho_cheio.filhos[grau:]
            filho_cheio.filhos = filho_cheio.filhos[:grau]

        pai.chaves.insert(indice_filho, chave_mediana)
        pai.filhos.insert(indice_filho + 1, novo_filho)

    def height(self) -> int:
        altura = 1
        atual = self._raiz

        while not atual.folha:
            altura += 1
            atual = atual.filhos[0]

        return altura

    def size(self) -> int:
        return self._tamanho

    def printLevels(self) -> list[list[list[T]]]:
        niveis: list[list[list[T]]] = []
        fila: list[NoArvoreB[T]] = [self._raiz]
        inicio = 0

        while inicio < len(fila):
            quantidade_nivel = len(fila) - inicio
            nivel: list[list[T]] = []

            for _ in range(quantidade_nivel):
                no = fila[inicio]
                inicio += 1

                nivel.append(no.chaves.copy())

                if not no.folha:
                    for filho in no.filhos:
                        fila.append(filho)

            niveis.append(nivel)

        return niveis

    def _inserir_nao_cheio(
        self,
        no: NoArvoreB[T],
        chave: T
    ):
        indice = len(no.chaves) - 1

        if no.folha:
            no.chaves.append(chave)

            while indice >= 0 and chave < no.chaves[indice]:
                no.chaves[indice + 1] = no.chaves[indice]
                indice -= 1

            no.chaves[indice + 1] = chave
            return

        while indice >= 0 and chave < no.chaves[indice]:
            indice -= 1

        indice += 1

        limite = (2 * self._grau_minimo) - 1

        if len(no.filhos[indice].chaves) == limite:
            self.split(no, indice)

            if chave > no.chaves[indice]:
                indice += 1

        self._inserir_nao_cheio(no.filhos[indice], chave)