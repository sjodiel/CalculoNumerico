import math

def f(x):
    return x**5 - 4*(x**2) + 2

def bissecao(f,a,b,eps):
    if f(a) * f(b) > 0:
        return ("Nenhuma raiz: os valores da função no estado inicial devem ser um sinal oposto.")
    else:
        #print("n", "  a", "  b", "    m", "    f(a)*f(m)", "|dx/2|")
        while True:
            x = (a + b) / 2.0
            dx = math.fabs((b - a) / 2.0)
            #print(n+1, "%.4f" % a, "%.4f" % b, "%.4f" % m, "+" if f(a) * f(m) > 0 else "-", "%.4f" % Dx)
            #return (n+1, "%.5f" % m, "%.5f" %f(m), (b-a)/2.0)
            if f(a) * f(x) < 0:
                b = x
            else:
                a = x
            #n += 1
            if dx < eps:
                break
        return x


b = 1.5
a = 0.8
eps = 1e-4
print( )
print("Raiz da funcao: ", "%.4f" % bissecao(f,a,b,eps))