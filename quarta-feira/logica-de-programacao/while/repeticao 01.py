ct = 0 
soma = 0
print ("digite (sair) para encerrar o programa")
while True: 
    numero = int(input("Digite um valor: ")) 
    if numero == -1:
     break 
    ct = ct + 1
    soma = soma + numero
print("A quantidade de valores digitados é:", ct)
print("A soma dos valores digitados é:", soma)