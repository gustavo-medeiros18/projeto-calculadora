# Exceção é um tipo de erro que pode acontecer
# durante a execução do nosso código, ou seja
# quando ele já está sendo executado pelo
# interpretador.

# Quando uma exceção ocorre, se ela não
# for tratada por nós, o interpretador
# interrompe a execução do nosso código,
# exibe uma mensagem mostrando a exceção que
# ocorreu, e em que parte do código ela ocorreu.

# Exemplo, temos uma lista de cinco divisores.
lista_divisores = [3, 6, 0, 9, 12]

# Com uma estrutura de repetição for, vamos
# percorrer a nossa lista, e dividir 36 por
# cada um dos divisores.
for item in lista_divisores:
    # Quando o divisor for zero, ocorrerá
    # uma exceção Division by zero. Nosso
    # programa não continuará as próximas
    # iterações (rodadas) do for quando isso
    # acontecer.
    print(f"Valor atual do item: {item}")

    resultado_divisao = 36 / item
    print(f"36 dividido por {item} = {resultado_divisao}")