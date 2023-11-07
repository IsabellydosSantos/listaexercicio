nome = str(input("Informe seu nome: "))
salf = int(input("Informe o valor do seu salário: "))
venda = int(input("Informe o número de vendas efetuadas nesse mês: "))

comis = venda*(salf*0.15)

salt = salf + comis

print("{}, seu salário fixo é {:.2f} reais, e seu salário final é {:.2f} reais".format (nome, salf, salt))