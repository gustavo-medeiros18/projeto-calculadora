# Tratamento de exceções consiste em
# implementar alguma estratégia no
# nosso código para que, caso um erro
# aconteça durante a execução, o programa
# possa reagir de maneira controlada
# (por exemplo, exibindo uma mensagem
# amigável ao usuário).

# Comandos dentro do try são aqueles que
# possuem chance de ocorrência de uma
# ou mais exceções.
try:
    numero = int(input("Digite um número: "))

    # Como já foi visto, caso o número
    # lido seja zero, ocorrerá uma exceção
    # ZeroDivisionError
    resultado = 100 / numero

    print(f"O resultado é {resultado}")
except ZeroDivisionError:
    # Este bloco será executado apenas quando
    # ocorrer uma exceção ZeroDivisionError.
    # Ou seja, quando tentarmos dividir por
    # zero.
    print("Não é possível dividir por zero.")
