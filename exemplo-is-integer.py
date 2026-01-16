# numero = 100.0
numero = float(input("Informe um número: "))

print("Tipo do número:", type(numero))
print("Número representa um inteiro?", numero.is_integer())

if numero.is_integer():
    print(f"{numero} é um float, mas representa um número inteiro.")

    numero_sem_decimal = int(numero)
    print(f"{numero} sem casas decimais: {numero_sem_decimal}")
else:
    print(f"{numero} tem parte decimal (não é inteiro).")