peso = float(input("Digite seu peso(kg):"))
altura = float(input("Digite sua altura:"))
imc = (peso / (altura * altura))
if imc  <= 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and  24.9:
    print("Peso adequado")
elif imc > 25 and  29.9:
    print("sobrepeso")
elif imc> 30:
    print("obesidade")
110.00
