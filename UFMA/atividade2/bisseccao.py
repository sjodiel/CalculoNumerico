import math

n = 3
eps = 10**(-3)
a = int(input("a: "))
b = int(input("b: "))


def f(x):
    return x**3 - 9*x + 3

def bisseccao(f,a,b,eps,n):
    #if f(a) * f(b) > 0:
     #   return ("Nenhuma raiz")
    #else:
        #print("n", "  a", "  b", "    m", "    f(a)*f(m)", "|dx/2|")
        i = 1
        fa = f(a)
        while i<=n:
            x = a + math.fabs((b - a) / 2.0)
            fp = f(a)
            #dx = math.fabs((b - a) / 2.0)
            #print(n+1, "%.4f" % a, "%.4f" % b, "%.4f" % m, "+" if f(a) * f(m) > 0 else "-", "%.4f" % Dx)
            #print(n+1, "%.5f" % m, "%.5f" %f(m), (b-a)/2.0)
            if (fp == 0 or (b-a)/2.0 < eps):
                print (x)
                break
            i+=1
            if fa * fp > 0:
                a=x
            else:
                b=x
        else:
            print ("O metodo falhou apos",n,"interacoes")

bisseccao(f,a,b,eps,n)