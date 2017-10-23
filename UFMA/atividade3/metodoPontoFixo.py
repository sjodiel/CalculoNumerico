import math

#Baseado no livro de Analise Numerica Burden

n = 31
eps = 5e-5
p0 = 1.5

def f(x):
    return x - x**3 - 4**2 + 10

def g(x):
    return (0.5)*(math.sqrt(x - (x**3) + 10))

def interacaoPontoFixo(g,p0,eps,n):
        i = 1
        while i<=n:
            p = g(p0)
            #print (p)
            #dx = math.fabs((b - a) / 2.0)
            #print(n+1, "%.4f" % a, "%.4f" % b, "%.4f" % m, "+" if f(a) * f(m) > 0 else "-", "%.4f" % Dx)
            #print(n+1, "%.5f" % m, "%.5f" %f(m), (b-a)/2.0)
            if (math.fabs(p - p0)) < eps: #f(p)<eps
                print (p)
                #print (f(p))
                break
            i+=1
            p0 = p

        else:
            print ("O metodo falhou apos",n,"interacoes")

interacaoPontoFixo(g,p0,eps,n)