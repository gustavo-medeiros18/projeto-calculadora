# range(1, 11) -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# item = 10
for item in range(1, 11):
    if item == 5:
        print("Item 5 encontrado, vou pular o resto do laço")
        continue

    print("Passou pelo item", item)
    print("Avançando para a próxima rodada...")

print("Saímos do for")