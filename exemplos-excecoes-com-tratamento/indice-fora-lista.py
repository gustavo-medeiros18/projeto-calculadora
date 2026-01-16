# Tratamento de exceções consiste em
# lidar com erros que podem acontecer
# durante a execução do programa,
# evitando que ele pare de forma inesperada.

lista = [10, 20, 30, 40]

# Comandos dentro do try são aqueles que
# possuem chance de ocorrência de uma
# ou mais exceções.
try:
    posicao = int(input("Qual posição da lista você quer acessar? "))

    # Como já foi visto, se a posição digitada
    # não existir na lista, ocorrerá uma exceção
    # IndexError.
    print(f"Elemento na posição {posicao}: {lista[posicao]}")
except IndexError:
    # Este bloco será executado somente quando
    # ocorrer uma exceção IndexError. Ou seja,
    # quando a posição escolhida estiver fora dos
    # limites da lista.
    print("Essa posição não existe na lista.")
