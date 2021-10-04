numero = int(input("Digite um número: "))
primeiro = 0
segundo = 0
while(primeiro < numero):
    primeiro = primeiro + segundo
    segundo = primeiro - segundo
    if primeiro ==0:
        primeiro = primeiro + 1
if primeiro == numero:
    print("Ação bem sucedida")
else:
    print("Ação falhou")