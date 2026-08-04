def converter_valor(texto: str):
    texto = texto.strip()

    try:
        return int(texto)
    except ValueError:
        pass

    try:
        return float(texto)
    except ValueError:
        return texto


def solicitar_inteiro(
    mensagem: str,
    minimo: int | None = None
) -> int:
    while True:
        try:
            valor = int(input(mensagem))

            if minimo is not None and valor < minimo:
                print(
                    f"Digite um valor maior ou igual a {minimo}."
                )
                continue

            return valor

        except ValueError:
            print("Digite um número inteiro válido.")


def exibir_elementos(elementos: list):
    if len(elementos) == 0:
        print("Estrutura vazia.")
        return

    print(elementos)
    