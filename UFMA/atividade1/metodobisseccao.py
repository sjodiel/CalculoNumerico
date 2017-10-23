import math

n = 0
eps = 10**(-3)
a = int(input("a: "))
b = int(input("b: "))


def f(x):
    return x**3 - 9*x + 3

def bisseccao(f,a,b,eps,n):
    if f(a) * f(b) > 0:
        print ("Nenhuma raiz")
    else:
        print("n", "  a", "  b", "    m", "    f(a)*f(m)", "|Dx/2|")
        while True:
            m = (a + b) / 2.0
            dx = math.fabs((b - a) / 2.0)
            #print(n+1, "%.4f" % a, "%.4f" % b, "%.4f" % m, "+" if f(a) * f(m) > 0 else "-", "%.4f" % Dx)
            print(n+1, "%.5f" % m, "%.5f" %f(m), (b-a)/2.0)
            if f(a) * f(m) < 0:
                b = m
            else:
                a = m
            n += 1
            if dx < eps:
                break

def bisseccao2(f,a,b,n):
    count = n
    while count > 0:
        x = (a+b)/2.0
        if f(a)*f(x) < 0:
            a=x
        elif f(a)*f(x) > 0:
            a=x
        else:
            break
        count=count-1
    return x