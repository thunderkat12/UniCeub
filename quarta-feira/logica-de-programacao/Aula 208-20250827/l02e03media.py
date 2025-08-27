"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

Crie um novo programa dentro do mesmo projeto no IDE PyCharm:
- Coluna esquerda - mouse direito no nome do projeto (PythonProject)
  New - Python File
- Digite o nome do programa Python sem espaço e sem acentuação - <Enter>

- Problema:

- Implemente o programa que calcule a média aritmética de duas notas
bimestrais fornecidas (digitadas) pelo usuário.

- Analise o problema e verifique quais dados de entrada o usuário precisa digitar.

- Fórmula de média aritmética = nota1 + nota2   (numerador)
                                      2         (denominador)

- Passos para resolver o problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: nota1: 4.5 e nota2: 6.1             Saída: 5.3
Teste 2: Entrada: nota1: 7.5 e nota2: 5.1             Saída: 6.3
Fim do Comentário de várias linhas.                 """

nota1 = float(input("Primeira nota: ")) # Converte os valores para float
nota2 = float(input("Segunda nota: "))
# Processamento, atribui o cálculo à variável media
media = (nota1 + nota2) / 2             # Parênteses obrigatórios.
print("Média:", media)                  # Mostra o resultado

''' --- ALTERAÇÕES:
a. Mostre a média com duas casas decimais
b. Acrescente, considere que o aluno realizou três avaliações. 
   Teste 3: Entrada: nota1: 2, nota2: 3 e nota3: 4       Saída: 3
c. Na execução, pule três linhas antes de mostrar o valor da média.
d. Depois da média, mostre também o valor das três notas.
e. Acrescente o cálculo da média ponderada, considerando que a nota1 
   tem peso 1, a nota2 tem peso 2 e a nota3 tem peso 3.  
   Teste com os valores 5, 6, 7.       A resposta certa é 6,3333333
f. Agora, refaça-o sem usar a variável media.     

    --- VEJA AS DICAS ABAIXO:
print(f'Média: {media:.2f}')  # Mostra com 2 casas decimais.    # a.
print('Média: {:.2f}' .format(media))  # Mostra com 2 casas decimais.
nota3 = float(input("Terceira nota: "))                         # b.
#   . . . 
media = (nota1 + nota2 + nota3) / 3
print ()                         # Solução 1                    # c.
print ()
print ()
print ('\n\n\n')                 # Solução 2                            
print("\n\n\nA média é", media)  # Solução 3                  
print ("Nota 1 =", nota1)                                       # d.
print ("Nota 2 =", nota2)                                      
print ("Nota 3 =", nota3)                                      
    . . .
media_pond = (nota1 * 1 + nota2 * 2 + nota3 * 3) / (1 + 2 + 3)  # e. 
Faça o cálculo dentro do print:                                 # f.
print ("Média:", (nota1 * 1 + nota2 * 2 + nota3 * 3) / (1 + 2 + 3) ) 
---

- Testes:
print("A média é", str(media))
print("A média é "+ str(media))

'''
