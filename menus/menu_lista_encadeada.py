from estruturas.lista_encadeada import ListaEncadeada
from menus.utilidades import (
    converter_valor,
    exibir_elementos,
)


def menu_lista_encadeada():
    lista = ListaEncadeada()

    while True:
        print("\n================================")
        print("Lista Encadeada Simples")
        print("================================")
        print("1 - Insert")
        print("2 - Remove")
        print("3 - Search")
        print("4 - Size")
        print("5 - IsEmpty")
        print("6 - ToArray")
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
                    input("Informe o elemento a remover: ")
                )

                removido = lista.remove(valor)
                print(f"Elemento removido: {removido}")

            elif opcao == "3":
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

            elif opcao == "4":
                print(f"Tamanho: {lista.size()}")

            elif opcao == "5":
                print(f"Lista vazia: {lista.isEmpty()}")

            elif opcao == "6":
                exibir_elementos(lista.toArray())

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

        except (IndexError, ValueError) as erro:
            print(erro)