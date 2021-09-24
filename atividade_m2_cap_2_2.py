plano = input("Qual o seu plano? Basic, Silver, Gold ou Platinum ")
fat = input("Qual seu faturamento anual em Reais? ")
plano = plano.upper()
fat = float(fat)
if plano == "BASIC":
    conta = fat * 0.3
    reais = round(conta, 2)
    print (" Sua conta saiu por R${} ".format(reais))
elif plano == "SILVER":
    conta = fat * 0.2
    reais = round(conta, 2)
    print (" Sua conta saiu por R${} ".format(reais))
elif plano == "GOLD":
    conta = fat * 0.1
    reais = round(conta, 2)
    print (" Sua conta saiu por R${} ".format(reais))
elif plano == "PLATINUM":
    conta = fat * 0.05
    reais = round(conta, 2)
    print (" Sua conta saiu por R${} ".format(reais))
else:
    print ("Erro, favor digitar o nome do plano corretamente")