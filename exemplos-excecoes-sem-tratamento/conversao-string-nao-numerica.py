# Exceção é um tipo de erro que pode acontecer
# durante a execução do nosso código, ou seja
# quando ele já está sendo executado pelo
# interpretador.

# Quando uma exceção ocorre, se ela não
# for tratada por nós, o interpretador
# interrompe a execução do nosso código,
# exibe uma mensagem mostrando a exceção que
# ocorreu, e em que parte do código ela ocorreu.

# Exemplo: estamos pedindo um número ao usuário.
# Como a função input sempre retorna o que foi
# lido na forma de uma string, é necessário
# converter para o tipo int.

# Caso a string lida não represente um número,
# ocorrerá uma exceção ValueError
numero = int(input("Digite um número: "))

print(f"O numero digitado foi: {numero}")