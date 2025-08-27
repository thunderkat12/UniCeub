"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:
- Elabore o programa que faça a conversão de graus Fahrenheit (ºF) para
graus Celsius (ºC).

- Fórmula:    celsius = 5 . (fahrenheit - 32)   (numerador)
                        9                       (denominador)
                   
- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para resolver o problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: Fahrenheit = 32   Saída: Celsius = 0.0
Teste 2: Entrada: Fahrenheit = 55   Saída: Celsius = 12.77777777777779
Teste 3: Entrada: Fahrenheit = 61   Saída: Celsius = 16.11111111111111

Fim do Comentário de várias linhas.
"""

# Recebe a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em ºF: "))
# Efetua o cálculo
celsius = 5 * (fahrenheit - 32) / 9  # Solução 1 (parênteses obrigatórios)
# celsius = 5 / 9 * (fahrenheit - 32)  # Solução 2
print("Graus em Celsius convertido", celsius)  # Mostra o resultado

''' --- ALTERAÇÕES:
a. Mostre o valor celsius com três casas decimais.
b. Altere o layout da mensagem de saída:
Valor em Fahrenheit: x.xx  (Mostrar com duas casas decimais).
Valor em Celsius: x.xxxx   (Mostrar com quatro casas decimais).
  
    --- Dicas abaixo:
print(f"Graus em Celsius convertido: {celsius:.3f} °C")                 # a.
#      Obs.: o valor 3 é a quantidade de casas decimais.
print("Graus correspondente em Celsius: {:.3f} °C" .format (celsius))  

print ("Valor em Fahrenheit: {:.2f}" .format(f))                       # b.
print ("Valor em Celsius: {:.4f}" .format(c))

'''
