import math

#Baseado no livro de Analise Numerica Burden


def metodoNewton(f,df,a,eps,n):
        i = 1
        while i<=n:
            x = a - float(f(a)/df(a))
            #dx = math.fabs((b - a) / 2.0)
            #print(n+1, "%.4f" % a, "%.4f" % b, "%.4f" % m, "+" if f(a) * f(m) > 0 else "-", "%.4f" % Dx)
            #print(n+1, "%.5f" % m, "%.5f" %f(m), (b-a)/2.0)
            if (math.fabs(x - a) < eps):
                print(x)
                break
            i+=1
            a = x
        else:
            print ("O metodo falhou apos",n,"interacoes")

#Questao 11
n = 1000
eps = 1e-4
a = 2.0

#Letra a f = x/2 - tg(x) =  0; df = 1/2 - sec**2(x) = 1/2 - 1/cos**2(x)

def f(x):
    return x/2 - math.tan(x)

def df(x):

    return 1/2 - 1/(math.pow(math.cos(x),2))

print("LETRA A")
metodoNewton(f,df,a,eps,n)

#Letra b: f = 2cos(x) = x**2/2 => 2cos(x) - e**2/2; df = -2sin(x) - e**2/2
def g(x):
    return 2*(math.cos(x)) - (math.pow(math.e,x))*(0.5)

def dg(x):
    return -2*(math.sin(x)) - (math.pow(math.e,x))*(0.5)

print("LETRA B")
metodoNewton(g,dg,a,eps,n)

#Letra c: f = x**5 - 6 e**2/2; df = -2sin(x) - e**2/2
def h(x):
    return x**5 - 6

def dh(x):
    return 5*(x**4)

print("LETRA C")
metodoNewton(h,dh,a,eps,n)
