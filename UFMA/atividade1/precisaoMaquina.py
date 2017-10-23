class precisao():
    a = 1.0
    s = 2.0

    while (s > 1):
        a /= 2 # a = a / 2
        s = 1 + a
        # print "s = ",s,"a = ",a
    prec = 2 * a
    print ("Precisao da Maquina = ", prec)

