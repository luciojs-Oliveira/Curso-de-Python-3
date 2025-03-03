
'''
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
escopo de variáveis e retorno de resultados.
'''






#Interactive help   = help() - função interna do python

#Modo de usar :
#ex : 01 abrir console e digitar help()
#ex : 02 usar help antes da função = (helpprint).
#ex : 03 imprimir o doc interno de um comando  = print(input.__doc__)
#mostra como funciona / metodo / funções / bibliotecas
#help(input.__doc__)
#help(input)



#DocsStrings
'''
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno.
    """
    c = i
    while c <= f:
        print(f' {c}', end='..')
        c += p
    print('FIM!')


#contador(2, 10, 2)
help(contador)
'''
'''
#Parametros opcionais
def somar(a, b, c=0):
    """
    -> Faz a soma de três números e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor.
    :param c: o terceiro valor.
    """
    
    s = a+b+c
    print(f'A soma vele{s}')


somar(3, 2, 5)
'''
#Escopo é o local onde a variavel vai existir e onde aa mesma não vai mais existir.
#Escopo de Váriaveis



#Argumentos



#Retorno de resultados

















