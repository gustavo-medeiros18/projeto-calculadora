# palavra = teclado
# palavra = mouse
# palavra = parar
while True:
    palavra = input("Informe uma palavra: ")

    if palavra == "parar":
        print("Pediu para parar. Saindo do while")
        break

    print("Avançando para a próxima rodada...")

print("Saímos do while")