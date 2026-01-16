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

valor_inicial = float(input("Digite o valor inicial: "))

while True:
    print(f"Resultado atual: {valor_inicial}")
    exibir_menu()

    opcao_escolhida = input("Escolha uma opção: ")

    if opcao_escolhida == "0":
        break

print("Encerrando a calculadora. Até mais!")