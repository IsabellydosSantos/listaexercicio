n1 = int(input("Informe um valor: "))
n2 = int(input("Informe um valor: "))
n3 = int(input("Informe um valor: "))
n4 = int(input("Informe um valor: "))
n5 = int(input("Informe um valor: "))

media = (n1+n2+n3+n4+n5)/5
maior = max(n1,n2,n3,n4,n5)
menor = min(n1,n2,n3,n4,n5)
 
print("O preço médio desses valores é {:.2f} reais, o maior preço é {:.2f} reais e o menor é {:.2f} reais".format(media, maior, menor))
 