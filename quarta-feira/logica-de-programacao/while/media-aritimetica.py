ct = 0    
soma = 0 
while True:
    numero = float(input("Digite a nota do aluno: "))
    if numero == -1:
        break
    ct = ct + 1
    soma = soma + numero
media = soma / ct    
print("A média aritmética dos valores digitados é:", media)
print("A quantidade de alunos:", ct)    