n = int(input("Informe um número de 0 a 9: "))
numext = {
0: "zero",
1: "um",
2: "dois",
3: "três",
4: "quatro",
5: "cinco",
6: "seis",
7: "sete",
8: "oito",
9: "nove"
}

if n >= 0 and n <=9:
 ext = numext[n]
 print("O número {} por extenso é {}".format(n, ext))
else:
 print("O número informado é inválido")