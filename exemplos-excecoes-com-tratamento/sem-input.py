# Tratamento de exceções consiste em
# lidar com erros que podem acontecer
# durante a execução do programa,
# evitando que ele pare de forma inesperada.

# Comandos dentro do try são aqueles que
# possuem chance de ocorrência de uma
# ou mais exceções.
try:
    # Essa operação sempre gera uma exceção
    # do tipo ZeroDivisionError.
    resultado_divisao = 100 / 0
except ZeroDivisionError:
    # Tratamos o erro exibindo uma mensagem
    # mais comunicativa ao usuário.
    print("Ocorreu uma divisão por zero no código.")
    print("Após o tratamento de exceção dentro do except")

print("Após a exceção")