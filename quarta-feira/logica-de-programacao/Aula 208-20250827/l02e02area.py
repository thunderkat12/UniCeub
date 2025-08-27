"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Operadores aritméticos:
    +   →   soma
    –   →   subtração
    *   →   multiplicação
    /   →   divisão
    //  →   divisão de inteiros (quociente da divisão)
    %   →   módulo (resto da divisão)
    **  →   potenciação

- IDE PyCharm:
1- Como criar um projeto:
   - File - New Project - Create
2- Como criar um programa dentro do projeto:
   - Coluna esquerda - mouse direito no nome do projeto (PythonProject)
   New - Python File
   - Digite o nome do programa Python sem espaço e sem acentuação - <Enter>
3- Como roda (executa) o programa:
   - Run - Run, ou use as teclas de atalho.

- Meet:     vbc-shqr-wxd

- Problema:

- Projete o programa para calcular a área de um triângulo. O usuário
informará (digitará) os dados necessários para o cálculo, ou seja,
a base e a altura do triângulo.

- Fórmula:     área = base . altura (numerador)
                            2       (denominador)

- Analise o problema e verifique quais dados de entrada o usuário precisa digitar.

- Passos para resolver o problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: base: 1.5 e altura: 2.6       Saída: 1.9500000000000002

Fim do Comentário de várias linhas.     """

# Calcular a área de um triângulo.
base = float(input("Digite a base: "))  # Recebe um valor real do usuário
altura = float(input("Digite a altura: "))
area = base * altura / 2                # Processamento
print("Área:", area)                    # Saída

''' --- ALTERAÇÕES:
a. Na tela de saída de dados, mostre também o valor da base e da altura.
b. Mostre o valor da área com três casas decimais.

----- DICAS ABAIXO:
print("Base:", base)                                            # a.
print("Altura:", altura)
print(f"Área: {area:.3f}")     # f-string       # Solução 1     # b.
print("Área: {:.3f}" .format(area))             # Solução 2     
print("Área: %.3f  " % (area))                  # Solução 3
# Obs.: o número 3 significa a quantidade de casas decimais.

----

print("Área:", round(area, 3))                  
Mostra com duas casas decimais:
1.95

'''
