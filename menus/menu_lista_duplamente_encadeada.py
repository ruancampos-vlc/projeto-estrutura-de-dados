from estruturas.lista_duplamente_encadeada import (
    ListaDuplamenteEncadeada,
)
from menus.utilidades import (
    converter_valor,
    exibir_elementos,
)


def menu_lista_duplamente_encadeada():
    lista = ListaDuplamenteEncadeada()

    while True:
        print("\n================================")
        print("Lista Duplamente Encadeada")
        print("================================")
        print("1 - Insert")
        print("2 - InsertFirst")
        print("3 - Remove")
        print("4 - RemoveFirst")
        print("5 - RemoveLast")
        print("6 - Search")
        print("7 - Size")
        print("8 - IsEmpty")
        print("9 - ToArray")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                valor = converter_valor(
                    input("Informe o elemento: ")
                )

                posicao_texto = input(
                    "Informe a posição ou Enter para o final: "
                ).strip()

                if posicao_texto == "":
                    lista.insert(valor)
                else:
                    lista.insert(valor, int(posicao_texto))

                print("Elemento inserido com sucesso.")

            elif opcao == "2":
                valor = converter_valor(
                    input("Informe o elemento: ")
                )

                lista.insertFirst(valor)
                print("Elemento inserido no início.")

            elif opcao == "3":
                valor = converter_valor(
                    input("Informe o elemento a remover: ")
                )

                removido = lista.remove(valor)
                print(f"Elemento removido: {removido}")

            elif opcao == "4":
                removido = lista.removeFirst()
                print(f"Elemento removido: {removido}")

            elif opcao == "5":
                removido = lista.removeLast()
                print(f"Elemento removido: {removido}")

            elif opcao == "6":
                valor = converter_valor(
                    input("Informe o elemento a buscar: ")
                )

                posicao = lista.search(valor)

                if posicao == -1:
                    print("Elemento não encontrado.")
                else:
                    print(
                        f"Elemento encontrado na posição {posicao}."
                    )

            elif opcao == "7":
                print(f"Tamanho: {lista.size()}")

            elif opcao == "8":
                print(f"Lista vazia: {lista.isEmpty()}")

            elif opcao == "9":
                exibir_elementos(lista.toArray())

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

        except (IndexError, ValueError) as erro:
            print(erro)