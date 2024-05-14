#folha de pagamento com descontos do FGTS, INSS

valor_hora=float(input("Valor de hora:"))
hora_trabalho=float(input('Horas de trabalho:'))

salario_bruto=valor_hora*hora_trabalho

if salario_bruto <= 900:
  fgts_desconto= salario_bruto* 0.05
  fgts= salario_bruto-fgts_desconto
  inss_desconto=fgts* 0.10
  inss=fgts-inss_desconto
  print(inss)
elif salario_bruto == 1500:
  fgts_desconto=salario_bruto * 0.05
  fgts= salario_bruto - fgts_desconto
  inss_desconto= fgts* 0.10
  inss= fgts - inss_desconto
  print(inss)
elif salario_bruto <= 2500:
  fgts_desconto= salario_bruto * 0.10
  fgts= salario_bruto- fgts_desconto
  inss_desconto= fgts * 0.10 
  inss= fgts - inss_desconto
  print(inss)
else:
  fgts_desconto= salario_bruto * 0.20
  fgts= salario_bruto - fgts_desconto
  inss_desconto= fgts * 0.10
  inss= fgts - inss_desconto
  print(inss)
  
  