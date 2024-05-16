soma_peso=0
cont= 0

for c in range (1,7):
  idade=int(input('Sua idade:'))
  peso=float(input('Seu peso:'))
  if idade == 1 or idade <=10:
    cont +=1
    soma_peso += peso
    media = soma_peso/cont
    print("Total de {}, na faixa de 1 aos 10.Media de {}".format(cont,media))
  elif idade == 11 or idade <=20:
    cont += 1
    soma_peso +=peso
    media = soma_peso / cont
    print("Total de {}, na faixa de 11 aos 20.Media de {}".format(cont,media))
  elif idade == 21 or idade <= 30:
    cont += 1
    soma_peso +=peso
    media= soma_peso / cont
    print("Total de {}, na faixa de 21 aos 30.Media de {}".format(cont,media))
  else:
    cont += 1
    soma_peso +=peso
    media= soma_peso / cont
    print("Total de {}, na faixa acima de 31.Media de {}".format(cont,media))
  