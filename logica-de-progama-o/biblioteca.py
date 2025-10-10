import random

numeroadv = random.randint(1,20)
vidas = 3
while True:
    useradv = int(input("Tente adivinhar ai doidin: "))
    if useradv == numeroadv:
        print("Acertou miseravi")
        print(f"Voce está com {vidas} vidas..")
        break
    elif useradv > numeroadv:
        print("Quase  neguin, é menor")
        vidas += -1
        print(f"Voce está com {vidas} vidas..")
    else:
        print("Quase neguin, é maior")
        vidas += -1   
        print(f"Voce está com {vidas} vidas..")
    if vidas == 0:
        print("Infelismente voce perdeu")
        print("0 vidas.")
        print(f"ta aqui teu numero neguin {numeroadv}")
        break    