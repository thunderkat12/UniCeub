"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

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

- Problema:
- Elabore o programa que calcule a soma de dois valores inteiros que serão
fornecidos (digitados) pelo usuário.

- Analise o problema e verifique quais dados de entrada o usuário precisa digitar.

- Passos para resolver o problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: Primeiro valor: 10            Saída: 30
                  Segundo valor: 20

Fim do Comentário de várias linhas.     """

# Recebe os valores convertidos para número inteiro
valor1 = int(input("Digite o primeiro valor: "))        # Entrada de dados
valor2 = int(input("Digite o segundo valor: "))
# Calcula e atribui o resultado à variável soma (processamento)
soma = valor1 + valor2
print("A soma é igual a", soma)                         # Saída

''' ----- ALTERAÇÕES:
a. No final do programa, acrescente a subtração dos valores lidos e
   mostre o resultado.
b. No final do programa, acrescente a multiplicação dos valores lidos e
   mostre o resultado. 
c. No final do programa, leia mais um valor inteiro, ou seja, o terceiro
   valor inteiro.
d. No final do programa, acrescente a soma dos três valores lidos e mostre
   o resultado.

    ----- DICAS:
subtracao = valor1 - valor2                             # a.
print("A subtração e igual a  ", subtracao)
multiplicacao = valor1 * valor2                         # b.
print("A multiplicação e igual a  ", multiplicacao)
valor3 = int(input("Digite o terceiro valor: "))        # c.
soma = valor1 + valor2 + valor3                         # d.
print("A soma é igual a  ", soma)

'''
