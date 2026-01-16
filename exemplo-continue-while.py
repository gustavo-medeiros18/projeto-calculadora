# numero = 0
while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    if numero < 0:
        print("Num. negativo ignorado. Vou pular o resto do laço.")
        continue

    print("Você digitou:", numero)

print("Loop encerrado")