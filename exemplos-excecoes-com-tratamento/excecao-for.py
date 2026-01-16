# Tratamento de exceções consiste em
# implementar alguma estratégia no
# nosso código para que, caso um erro
# aconteça durante a execução, o programa
# possa reagir de maneira controlada
# (por exemplo, exibindo uma mensagem
# amigável ao usuário).

# Exemplo, temos uma lista de cinco divisores.
lista = [3, 6, 0, 9, 12]

# Com uma estrutura de repetição for, vamos
# percorrer a nossa lista, e dividir 36 por
# cada um dos divisores.

# item = 12
# resultado_divisao = 3.0
for item in lista:
    try:
        # Quando o divisor for zero, ocorrerá
        # uma exceção Division by zero. Nosso
        # programa não continuará quando isso
        # acontecer.
        resultado_divisao = 36 / item

        print(f"36 dividido por {item} = {resultado_divisao}")
    except ZeroDivisionError:
        # Este bloco será executado apenas quando
        # ocorrer uma exceção ZeroDivisionError.
        # Ou seja, quando tentarmos dividir por
        # zero.

        # Como a exceção está sendo tradada nesse
        # bloco except, o programa retomará as
        # iterações (rodadas) seguintes do for.
        print("Ocorreu uma divisão por zero")

print("Encerrei o for")