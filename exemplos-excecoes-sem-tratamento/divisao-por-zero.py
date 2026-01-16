# Exceção é um tipo de erro que pode acontecer
# durante a execução do nosso código, ou seja
# quando ele já está sendo executado pelo
# interpretador.

# Quando uma exceção ocorre, se ela não
# for tratada por nós, o interpretador
# interrompe a execução do nosso código,
# exibe uma mensagem mostrando a exceção que
# ocorreu, e em que parte do código ela ocorreu.

# Exemplo: estamos pedindo um número ao usuário
# e vamos dividir 100 por esse número lido.
# Caso o número lido seja zero, isso vai
# desencadear um erro.
numero = int(input("Digite um número: "))

# Se o numero lido foi zero, ocorrerá uma
# exceção ZeroDivisionError
resultado = 100 / numero

print(f"O resultado é {resultado}")
