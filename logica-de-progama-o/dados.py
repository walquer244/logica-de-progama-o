#contar pares e impares 
contapar = 0
contaimpar = 0
# numeros = int(input("Digite 10 numeros diferentes"))
for i in range(3):
    numeros = int(input("Digite numeros diferentes"))
    if numeros %2 == 0 :
        contapar += 1
    elif numeros %2 != 0:
        contaimpar += 1
print(contaimpar)
print(contapar)            