def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def exibir_menu():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

resultado_atual = float(input("Digite o valor inicial: "))

while True:
    print(f"Resultado atual: {resultado_atual}")
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ")

    if opcao_escolhida == "0":
        break

    valor_operando = float(input("Digite o próximo valor do operando: "))

    if opcao_escolhida == "1":
        resultado_atual = soma(resultado_atual, valor_operando)
    elif opcao_escolhida == "2":
        resultado_atual = subtracao(resultado_atual, valor_operando)
    elif opcao_escolhida == "3":
        resultado_atual = multiplicacao(resultado_atual, valor_operando)
    elif opcao_escolhida == "4":
        resultado_atual = divisao(resultado_atual, valor_operando)


print("Encerrando a calculadora. Até mais!")