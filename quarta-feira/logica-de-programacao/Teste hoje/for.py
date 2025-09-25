soma = 0
produto = 1
ct = 0
final = int(input("valor final da saquencia de naturais:"))
print("\nSequencia gerada:")
for valor in range(0, final+1, 1):
    soma += valor
    ct += 1
    media = soma / ct

print(final)
print(ct)
print(media)