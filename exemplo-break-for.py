# item = 1
# item = 2
# item = 3
# item = 4
# item = 5
for item in range(1, 11):
    print("Passando pelo item", item)

    if item == 5:
        print("Item 5 encontrado. Saindo do for")
        break

    print("Avançando para a próxima rodada...")

print("Saímos do for")