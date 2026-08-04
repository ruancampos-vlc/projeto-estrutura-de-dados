from estruturas.arvore_avl import ArvoreAVL
from menus.utilidades import (
    converter_valor,
    exibir_elementos,
)


def menu_arvore_avl():
    arvore = ArvoreAVL()

    while True:
        print("\n================================")
        print("Árvore AVL")
        print("================================")
        print("1 - Insert")
        print("2 - Remove")
        print("3 - Search")
        print("4 - GetRoot")
        print("5 - Height")
        print("6 - Size")
        print("7 - IsEmpty")
        print("8 - Minimum")
        print("9 - Maximum")
        print("10 - PreOrder")
        print("11 - Order")
        print("12 - PostOrder")
        print("13 - Fator de balanceamento da raiz")
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
                print(
                    f"Menor elemento: {arvore.minimum().valor}"
                )

            elif opcao == "9":
                print(
                    f"Maior elemento: {arvore.maximum().valor}"
                )

            elif opcao == "10":
                exibir_elementos(arvore.preOrder())

            elif opcao == "11":
                exibir_elementos(arvore.order())

            elif opcao == "12":
                exibir_elementos(arvore.postOrder())

            elif opcao == "13":
                raiz = arvore.getRoot()

                if raiz is None:
                    print("A árvore está vazia.")
                else:
                    fator = arvore.calculate_balance(raiz)
                    print(
                        "Fator de balanceamento da raiz: "
                        f"{fator}"
                    )

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

        except (IndexError, TypeError, ValueError) as erro:
            print(erro)