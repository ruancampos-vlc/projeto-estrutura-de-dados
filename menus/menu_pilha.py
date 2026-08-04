from estruturas.pilha import Pilha
from menus.utilidades import (
    converter_valor,
    exibir_elementos,
    solicitar_inteiro,
)


def menu_pilha():
    capacidade = solicitar_inteiro(
        "\nInforme a capacidade da pilha: ",
        minimo=1
    )

    pilha = Pilha(capacidade)

    while True:
        print("\n==========================")
        print("Pilha")
        print("==========================")
        print("1 - Push")
        print("2 - Pop")
        print("3 - Top")
        print("4 - IsEmpty")
        print("5 - IsFull")
        print("6 - Exibir elementos")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                valor = converter_valor(
                    input("Informe o elemento: ")
                )

                pilha.push(valor)
                print("Elemento inserido com sucesso.")

            elif opcao == "2":
                elemento = pilha.pop()
                print(f"Elemento removido: {elemento}")

            elif opcao == "3":
                print(f"Elemento do topo: {pilha.top()}")

            elif opcao == "4":
                print(f"Pilha vazia: {pilha.isEmpty()}")

            elif opcao == "5":
                print(f"Pilha cheia: {pilha.isFull()}")

            elif opcao == "6":
                exibir_elementos(pilha.toArray())

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

        except (IndexError, OverflowError, ValueError) as erro:
            print(erro)