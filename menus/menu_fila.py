from estruturas.fila import Fila
from menus.utilidades import (
    converter_valor,
    exibir_elementos,
    solicitar_inteiro,
)


def menu_fila():
    capacidade = solicitar_inteiro(
        "\nInforme a capacidade da fila: ",
        minimo=1
    )

    fila = Fila(capacidade)

    while True:
        print("\n==========================")
        print("Fila")
        print("==========================")
        print("1 - Enqueue")
        print("2 - Dequeue")
        print("3 - Head")
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

                fila.enqueue(valor)
                print("Elemento inserido com sucesso.")

            elif opcao == "2":
                elemento = fila.dequeue()
                print(f"Elemento removido: {elemento}")

            elif opcao == "3":
                print(f"Primeiro elemento: {fila.head()}")

            elif opcao == "4":
                print(f"Fila vazia: {fila.isEmpty()}")

            elif opcao == "5":
                print(f"Fila cheia: {fila.isFull()}")

            elif opcao == "6":
                exibir_elementos(fila.toArray())

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")

        except (IndexError, OverflowError, ValueError) as erro:
            print(erro)