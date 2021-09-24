seg = input ("Quantos votos foram dados na Segunda-feira  ")
ter = input ("Quantos votos foram dados na Terça-feira  ")
qua = input ("Quantos votos foram dados na Quarta-feira  ")
qui = input ("Quantos votos foram dados na Quinta-feira  ")
sex = input ("Quantos votos foram dados na Sexta-Feira  ")
if seg > ter and seg > qua and seg > qui and seg > sex:
    print ("Segunda-Feira foi a mais votada com {} votos".format(seg))
elif ter > seg and ter > qua and ter > qui and ter > sex:
    print ("Terça-Feira foi a mais votada com {} votos".format(ter))
elif qua > seg and qua > ter and qua > qui and qua > sex:
    print ("Quarta-Feira foi a mais votada com {} votos".format(qua))
elif qui > seg and qui > ter and qui > qua and qui > sex:
    print ("Quinta-Feira foi a mais votada com {} votos".format(qui))
elif sex > seg and sex > ter and sex > qua and sex > qui:
    print ("Sexta-Feira foi a mais votada com {} votos".format(sex))
else:
    print ("Houve um empate, uma nova votação será necessária!")