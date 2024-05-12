#Dada uma string scomposta por palavras e espaços, retorne o comprimento da última palavra da string.Uma palavra é um máximo substring consistindo apenas em caracteres sem espaço.
palavra=str(input('Digite uma palavra: '))

array=palavra.split()

print("A ultima palavra é {} com comprimento {}".format(array[-1],len(array[-1])))

