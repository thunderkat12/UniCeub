"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha

- Meet:     vbc-shqr-wxd

- Problema:

- Refaça o programa que calcule a média aritmética de um aluno que
realizou duas avaliações. Além do valor da média, inclua na tela de
saída uma das mensagens: “Aluno aprovado.” ou “Aluno reprovado.”.
Considere que o aluno será aprovado com a média maior ou igual a cinco.

- Fórmula:  média = nota1 + nota2   (numerador)
                          2         (denominador)

- Analise o problema e verifique quais dados de entrada o usuário precisa digitar.

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Testes (se ...)
Saída de dados (escreva)

- Sintaxe do if ... else:
if condicao1:            # A indentação é obrigatória.
    print(“Mensagem 1”)  # Executa, se a condição1 for verdadeira
else:
    print("Mensagem 3")  # Executa, se todos os testes anteriores forem falsos.
Obs.: na linha do "else:" nunca colocar uma condição (um teste)

Teste 1: Entrada: nota1 = 5, nota2 = 2         Saída: Média = 3.5
                                                      Aluno reprovado.
Teste 2: Entrada: nota1 = 5.5, nota2 = 6.5     Saída: Média = 6.0
                                                      Aluno aprovado
"""

# Leia um valor, converta para float e atribua à variável nota1
nota1 = float(input("Primeira nota: "))
# Leia um valor, converta para float e atribua à variável nota2
nota2 = float(input("Segunda nota: "))
# Atribui o resultado do cálculo à variável media
media = (nota1 + nota2) / 2    # Parênteses obrigatórios
print('Média aritmética =', media)
if media >= 5:
    print("Aluno aprovado.")   # Imprime se a média for maior ou igual a 5
else:
    print("Aluno reprovado.")  # Imprime se a condição do if for falsa

''' ----- ALTERAÇÕES:
a. Mostre o valor da média aritmética com duas casas decimais.
b. Altere a saída. Mostre a média e a mensagem na mesma linha:
   Média do aluno: x.xxx           Aluno aprovado ou Aluno reprovado
c. Refaça-o considerando que a primeira prova tem peso três e
   a segunda, peso cinco. Ou seja, calcula a média ponderada do aluno.
   Teste 3: nota1 = 5, nota2=6, peso1=3, peso2=5      Saída: média = 5,625

   ----- DICAS ABAIXO:
print (f'Média = {media:.2f}')       # Mostra com 2 casas decimais.    # a.
print ('Média = {:.2f}' .format (media) )               Solução 2  
print ('Média = %.2f' % (media) )                       Solução 3
if media >=5:                                                          # b.
    print("Média = ", media, "Aluno aprovado.")              # Solução 1
    # print(f"Média = {media:.2f} Aluno aprovado")           # Solução 2
    # print("Média = {:.2f} Aluno aprovado" .format(media))  # Solução 3
else:                                                          
    print("Média = {:.2f}   Aluno reprovado" .format(media))           
media = (nota1 * 3 + nota2 * 5) / (3 + 5)  # Parênteses obrigatórios.  # c.

'''
