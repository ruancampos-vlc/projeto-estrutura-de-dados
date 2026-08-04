from estruturas.arvore_binaria_busca import (
    ArvoreBinariaBusca,
)
from menus.utilidades import (
    converter_valor,
    exibir_elementos,
)


def menu_arvore_binaria_busca():
    arvore = ArvoreBinariaBusca()

    while True:
        print("\n================================")
        print("Árvore Binária de Busca")
        print("================================")
        print("1 - Insert")
        print("2 - Remove")
        print("3 - Search")
        print("4 - GetRoot")
        print("5 - Height")
        print("6 - Size")
        print("7 - IsEmpty")
        print("8 - PreOrder")
        print("9 - Order")
        print("10 - PostOrder")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                valor = converter_valor(
                    input("Informe o elemento: ")
                )

                arvore.insert(valor)
                print("Elemento inserido com sucesso.")

            elif opcao == "2":
                valor = converter_valor(
                    input("Informe o elemento a remover: ")
                )

                removido = arvore.remove(valor)
                print(f"Elemento removido: {removido}")

            elif opcao == "3":
                valor = converter_valor(
                    input("Informe o elemento a buscar: ")
                )

                no = arvore.search(valor)

                if no is None:
                    print("Elemento não encontrado.")
                else:
                    print("Elemento encontrado.")

            elif opcao == "4":
                raiz = arvore.getRoot()

                if raiz is None:
                    print("A árvore está vazia.")
                else:
                    print(f"Raiz: {raiz.valor}")

            elif opcao == "5":
                print(f"Altura: {arvore.height()}")

            elif opcao == "6":
                print(f"Tamanho: {arvore.size()}")

            elif opcao == "7":
                print(f"Árvore vazia: {arvore.isEmpty()}")

            elif opcao == "8":
                exibir_elementos(arvore.preOrder())

            elif opcao == "9":
                exibir_elementos(arvore.order())

            elif opcao == "10":
                exibir_elementos(arvore.postOrder())

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

        except (IndexError, TypeError, ValueError) as erro:
            print(erro)