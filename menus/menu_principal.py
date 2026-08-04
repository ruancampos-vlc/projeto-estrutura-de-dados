from menus.menu_arvore_avl import menu_arvore_avl
from menus.menu_arvore_b import menu_arvore_b
from menus.menu_arvore_binaria_busca import (
    menu_arvore_binaria_busca,
)
from menus.menu_fila import menu_fila
from menus.menu_lista_duplamente_encadeada import (
    menu_lista_duplamente_encadeada,
)
from menus.menu_lista_encadeada import menu_lista_encadeada
from menus.menu_pilha import menu_pilha


def exibir_menu():
    print("\n===================================")
    print("Biblioteca de Estruturas de Dados")
    print("===================================")
    print("1 - Pilha")
    print("2 - Fila")
    print("3 - Lista Encadeada Simples")
    print("4 - Lista Duplamente Encadeada")
    print("5 - Árvore Binária de Busca")
    print("6 - Árvore AVL")
    print("7 - Árvore B")
    print("0 - Encerrar")


def menu_principal():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_pilha()

        elif opcao == "2":
            menu_fila()

        elif opcao == "3":
            menu_lista_encadeada()

        elif opcao == "4":
            menu_lista_duplamente_encadeada()

        elif opcao == "5":
            menu_arvore_binaria_busca()

        elif opcao == "6":
            menu_arvore_avl()

        elif opcao == "7":
            menu_arvore_b()

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")