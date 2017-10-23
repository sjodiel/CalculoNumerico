import math

#Baseado no livro de Analise Numerica Burden

n = 100
eps = 5e-15
#a = int(input("a: "))
#b = int(input("b: "))
a = 0.0
b = 1.1

def f(x):
    return math.cos(x) - x

def metodofalsaPosicao(f,a,b,eps,n):
        i = 2
        q0,q1=f(a),f(b)

        while i<=n:
            x = b - q1*(b - a)/(q1-q0)
            #dx = math.fabs((b - a) / 2.0)
            #print(n+1, "%.4f" % a, "%.4f" % b, "%.4f" % m, "+" if f(a) * f(m) > 0 else "-", "%.4f" % Dx)
            #print(n+1, "%.5f" % m, "%.5f" %f(m), (b-a)/2.0)
            if (math.fabs(x - b) < eps):
                print (x)
                break
            i+=1
            q = f(x)
            if q * q1 < 0:
                a=b
                q0=q1

            b = x
            q1 = q

        else:
            print ("O metodo falhou apos",n,"interacoes")

metodofalsaPosicao(f,a,b,eps,n)