# Exceção é um tipo de erro que pode acontecer
# durante a execução do nosso código, ou seja
# quando ele já está sendo executado pelo
# interpretador.

# Quando uma exceção ocorre, se ela não
# for tratada por nós, o interpretador
# interrompe a execução do nosso código,
# exibe uma mensagem mostrando a exceção que
# ocorreu, e em que parte do código ela ocorreu.

# Exemplo: temos uma lista de quatro
# elementos. Estamos pedindo ao usuário
# um número de uma posição na lista para
# acessarmos.
lista = [10, 20, 30, 40]
posicao = int(input("Qual posicao da lista você quer acessar? "))

# Se a posição lida estiver "fora dos limites"
# da lista, ocorrerá uma exceção IndexError
print(f"Elemento na posicao {posicao}: {lista[posicao]}")
print("Após mostrar o elemento")