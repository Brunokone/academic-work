altura = float(input("Qual a sua altura em cm? "))
peso = float(input("Quantos kg você pesa? "))
altm = altura /100
bimc =(altm * altm)
imc = peso / bimc
print ( "Seu imc é {}".format(imc))
if imc >= 40:
    print("Voçe está na faixa de Obesidade Grau 3")
elif (imc) >= 35:
    print("Você está na faixa de Obesidade Grau 2")
elif (imc) >= 30:
    print("Você está na faixa de Obesidade Grau 1")
elif (imc) >= 25:
    print("Você está na faixa de Sobrepeso")
elif (imc) >= 18.5:
    print("Você está na faixa de Peso ideal, Parabéns")
elif (imc) >= 17:
    print("Você está na faixa de Baixo peso Grau 1")
elif (imc) >= 16:
    print("Você está na faixa de Baixo peso Grau 2")
else:
    print("Você está na faixa de Baixo peso Grau 3")