ct = 0
soma = 0 
ct_impares = 0
ct_pares = 0

while True:
     numero = int(input("digite um numero ou zero para encerrar:"))   
     if numero == 0:
        break
     ct = ct +1
     soma = soma + numero
     
     if numero % 2 == 1:
         ct_impares +=1
     else:
         ct_pares += 1   
media = soma / ct 
    
print("valores digitados:", ct , "a soma dos valores:", soma , "a quantidades de de numeros digitados impares", ct_impares, "e valores pares ", ct_pares, "e a media é:", media)