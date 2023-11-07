raio = float(input("Informe o raio do tanque(em m): "))
alt = float(input("Informe a altura do tanque(em m): "))

areabase = 3.14 * (raio**2)
arealateral = ((2*3.14)*raio)*alt
areatotal = (2*areabase) + arealateral

#cada lata cobre 15m

lata = areatotal / 15
lata = round(lata)

preco = lata * 50

print("Serão necessárias {} latas e vai sair por {} reais".format(lata, preco))

