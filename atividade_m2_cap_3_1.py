refeicao = int(input("Quantas vezes você comeu hoje? : "))
calotot = 0
for q in range (0, refeicao):
    caloref = int(input("Quantas calorias tinha a porção? : "))
    calotot = caloref + calotot
print ("Você ingeriu {} calorias hoje".format(calotot))