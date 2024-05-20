media_idade=0
cont=0
idade_atual=0
nomehomem=0
contmulher=0
print('Digite:\n1-Feminino\n2-Masculino')

for c in range (1,4):
  nome= str(input('{}ª nome:'.format(c)))
  idade=int(input('Idade:'))
  sexo=str(input('Sexo:'))
  
  media_idade+=idade
  media=media_idade/c
  if c == 1 and sexo in 'Mm':
    nomehomem= nome
    idade_atual=idade
  if sexo in 'Mm' and idade > idade_atual:
      nomehomem=nome
      idade_atual=idade
  if sexo in 'Ff' and idade < 20:
      cont+=1
  if sexo !=  'fF' or 'Mm':
    print('erro')
    break
print ('media {}'.format(media))
print('Homem mais velho {} idade {}'.format(nomehomem,idade_atual))
print('mulheres {}'.format(cont))