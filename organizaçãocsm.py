"""As organizações CSM resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. 
a. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual; 
b. Salários até R$ 280,00 (incluindo): aumento de 20%;
c. Salários entre R$ 280,00 e R$700,00: aumento de 15%;
d. Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%;
e. Salários de R$ 1500,00 em diante: aumento de 5%
Após o aumento ser realizado; informe na tela;
a. O salário antes do reajuste;
b. O percentual de aumento aplicado;
c. O valor do aumento;
d. O novo salário, após o aumento"""


salario=float(input('Salario Bruto: '))

if salario < 280:
  perc_aument= salario*0.20
  aumento=salario + perc_aument
  print('Salario antes: {:.2f} \n Percentual: 20% \n Valor do aumento: {:.2f} \n Novo Salario: {:.2f}'.format(salario,perc_aument, aumento))
elif salario > 280 and salario < 700:
  perc_aument=salario*0.15
  aumento=salario + perc_aument
  print('Salario antes: {:.2f} \n Percentual: 15%\n Valor do Aumento: {:.2f} \n Novo Salario: {:.2f}'.format(salario,perc_aument,aumento))
elif salario > 700 and salario < 1500:
  perc_aument= salario * 0.10
  aumento= salario + perc_aument
  print('Salario antes: {:.2f} \n Percentual: 10%\n Valor do Aumento: {:.2f} \n Novo Salario: {:.2f}'.format(salario,perc_aument,aumento))
else:
  perc_aument=salario * 0.05
  aumento= salario + perc_aument
  print('Salario antes: {:.2f} \n Percentual: 5%\n Valor do Aumento: {:.2f} \n Novo Salario: {:.2f}'.format(salario,perc_aument,aumento))