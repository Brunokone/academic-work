quant = int(input("Quantas vezes voçê comprou algo hoje? : "))
medgast =float (0)
for q in range (0, quant):
    gasto = float(input("Quanto foi gasto na compra? :"))
    medgast = gasto + medgast
medfinal = medgast / quant
media = round(medfinal, 2)
print ("Hoje você gastou R${}, com uma média de R${} por compra.".format(medgast, media))