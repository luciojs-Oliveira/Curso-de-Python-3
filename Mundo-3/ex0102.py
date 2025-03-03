def fatorial(n, show=False):

    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcinal) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for count in range(n, 0, -1):
        if show:
            print(count, end='')
            if count > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= count
    return f


# Programa Principal
print(fatorial(5, show=True))
help(fatorial)
