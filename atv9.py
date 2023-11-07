nome = str(input("Informe seu nome: "))
sal = float(input("Informe seu salário atual: "))
reaj = float(input("Informe a porcentagem do reajuste anual: "))

salre = sal + (sal*(reaj/100))

print("{} seu salário reajustado é igual a {:.2f} reais".format(nome, salre))