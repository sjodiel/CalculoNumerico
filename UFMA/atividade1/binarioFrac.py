def floatpoint(num, prec):
    # fracionario recebe a parte fracionaria do numero digitado
    frac = num
    mult = 0.1
    fracaoBin = 0.0

    if (num >= 1 or num < 0):
        print("Erro: O numero deve estah entre 0...1")
    else:
        # converte a parte fracionaria para binario
        i = 0
        while (i != prec):
            frac *= 2
            if (frac >= 1):
                frac -= 1
                fracaoBin += mult
            mult /= 10
            i += 1
        # total = fracaoBin
        print(fracaoBin)
        # return fracaoBin



# teste
n = 0.1233333
p = 7

floatpoint(n, p)
