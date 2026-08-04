from estruturas.arvore_b import ArvoreB
from menus.utilidades import (
    converter_valor,
    solicitar_inteiro,
)


def menu_arvore_b():
    grau_minimo = solicitar_inteiro(
        "\nInforme o grau mínimo da Árvore B: ",
        minimo=2
    )

    arvore = ArvoreB(grau_minimo)

    while True:
        print("\n================================")
        print("Árvore B")
        print("================================")
        print("1 - Insert")
        print("2 - Search")
        print("3 - Height")
        print("4 - Size")
        print("5 - PrintLevels")
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
                    input("Informe o elemento a buscar: ")
                )

                if arvore.search(valor):
                    print("Elemento encontrado.")
                else:
                    print("Elemento não encontrado.")

            elif opcao == "3":
                print(f"Altura: {arvore.height()}")

            elif opcao == "4":
                print(f"Tamanho: {arvore.size()}")

            elif opcao == "5":
                niveis = arvore.printLevels()

                for indice, nivel in enumerate(niveis):
                    print(f"Nível {indice}: {nivel}")

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

        except (TypeError, ValueError) as erro:
            print(erro)