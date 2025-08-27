"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:

- Projete o programa que leia um valor numérico e verifique se ele é maior
ou igual a cem. Mostre uma das mensagens: “Valor maior ou igual a cem.” ou
“Valor menor que cem.”

- Analise o problema e verifique quais dados de entrada o usuário precisa digitar.

- Passos para resolver o problema (algoritmo):
Entrada de dados (leia)
[Processamento (cálculo)]               # Opcional
Testes (se ...)
Saída de dados (escreva)

- Sintaxe do if ... else:
if condicao1:            # A indentação é obrigatória.
    print(“Mensagem 1”)  # Executa, se a condição1 for verdadeira
else:
    print("Mensagem 3")  # Executa, se todos os testes anteriores forem falsos.
Obs.: na linha do else: nunca colocar uma condição (um teste)

Teste 1: Entrada: valor = 200           Saída: Valor maior ou igual a cem.
Teste 2: Entrada: valor = 20            Saída: Valor menor que cem.
Teste 3: Entrada: valor = 100           Saída: Valor maior ou igual a cem.

"""

valor = int(input("Digite um número: "))  # Recebe um número digitado
# Verifica se valor >= 100 para mostrar a mensagem
if valor >= 100:                          # Obrigatório usar os dois pontos [:]
    print("Valor maior ou igual a cem.")  # Indentação (to indent) obrigatória.
else:                                     # Caso não seja verdade
    print("Valor menor que cem.")

''' --- ALTERAÇÕES:
a. Além da mensagem, mostre também na saída o número digitado pelo usuário.

    --- DICAS ABAIXO:
print("Valor lido:", valor)                     # Solução 1               # a.
print(f"O seu número foi: {valor}")             # Solução 2, f-string
print("O seu número foi: {}" .format(valor))    # Solução 3, format

'''
