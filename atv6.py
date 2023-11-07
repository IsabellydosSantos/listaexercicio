custf = float(input("Informe o valor de fábrica do carro: "))

imp = custf + (custf*0.45) #imposto no custo de fábrica
custc = imp + (imp * 0.28)

print("O custo de fábrica do carro é {:.2f} reais, e o custo ao consumidor é de {:.2f} reais".format(custf, custc))