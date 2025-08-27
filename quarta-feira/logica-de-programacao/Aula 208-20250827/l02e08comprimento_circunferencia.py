"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema:

- Elabore o programa que calcula o comprimento de uma circunferência.
  O usuário fornecerá o dado necessário.

- Onde:
comprimento = 2 . π . raio

- Passos para resolver o problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: raio: 2       Saída: Comprimento: 12.56
Teste 2: Entrada: raio: 3       Saída: Comprimento: 18.84

"""
# Comprimento circurferência

raio = float(input("Digite o raio: "))
comprimento = 2 * 3.14 * raio
print("Comprimento:", comprimento)


"""
--- Alterações:
a. Mostre a saída com três casas decimais
b. Refaça usando o valor de pi da função math

--- Dicas:
print(f"Comprimento: {comprimento:.3f}")                    # a.
print("Comprimento: %.3f" % comprimento)

import math                                                 # b.
raio = float(input("Digite o raio: "))
comprimento = 2 * math.pi * raio

"""