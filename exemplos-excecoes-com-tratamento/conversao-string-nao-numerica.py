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
    # Como já foi visto, caso a string lida
    # não represente um número, ocorrerá uma
    # exceção ValueError
    numero = int(input("Digite um número: "))

    print(f"O número digitado foi: {numero}")
except ValueError:
    # Este bloco será executado apenas se
    # ocorrer uma exceção do tipo ValueError,
    # ou seja, quando a string digitada
    # não puder ser convertida para número.
    print("Este valor não é um número válido.")
