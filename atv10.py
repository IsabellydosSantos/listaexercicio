alt = int(input("Informe a altura do triângulo: "))
print("Informe os valores dos lados do triângulo")
l1 = int(input("Lado 1(base): "))
l2 = int(input("Lado 2: "))
l3 = int(input("Lado 3: "))

area = (l1*alt)/2

if l1==l2 and l2==l3:
    print("Esse é um triângulo equilátero, sua área é igual a: {} metros quadrados".format(area))
elif l1==l2 or l2==l3 or l1==l3:
    print("Esse é um triângulo isóceles, sua área é igual a: {} metros quadrados".format(area))
else:
    print("Esse é um triângulo escaleno, sua área é igual a: {} metros quadrados".format(area))
