escolha = input("Escolha a conversão (R se for de real para dólar, D se for ao contrário):").upper()

if escolha == 'R':
    real = float(input("Informe o valor em real para ser convertido: "))
    dolara = float(input("Informe a taxa do dólar atualmente: "))
    valdol = real / dolara
    
    print('O valor em dólar é de: U$$ ', valdol)

elif escolha == 'D':
    dolar = float(input("Informe o valor em dólar para ser convertido: "))
    reala = float(input("Informe a taxa do real atualmente: "))
    valreal = dolar * reala

    print('O valor em real é de: R$ ', valreal)