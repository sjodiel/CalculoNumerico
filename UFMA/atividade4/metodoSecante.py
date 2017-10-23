import math

#Baseado no livro de Analise Numerica Burden

def metodoSecante(f,a,b,eps,n):
        i = 2
        q0,q1=f(a),f(b)

        while i<=n:
            x = b - q1*(b - a)/(q1-q0)
            #dx = math.fabs((b - a) / 2.0)
            #print(n+1, "%.4f" % a, "%.4f" % b, "%.4f" % m, "+" if f(a) * f(m) > 0 else "-", "%.4f" % Dx)
            #print(n+1, "%.5f" % m, "%.5f" %f(m), (b-a)/2.0)
            if (math.fabs(x - b) < eps):
                print (x)
                #print(f(x))
                break
            i+=1

            a = b
            q0 = q1
            b = x
            q1 = f(b)

        else:
            print ("O metodo falhou apos",n,"interacoes")

#Questao 11
n = 100
eps = 1e-4
a = 1.0
b = 2.0

#Letra a f = x/2 - tg(x) =  0; df = 1/2 - sec**2(x) = 1/2 - 1/cos**2(x)

def f(x):
    return x/2 - math.tan(x)

print("LETRA A")

metodoSecante(f,1.0,2.0,eps,n)

#Letra b: f = 2cos(x) = x**2/2 => 2cos(x) - e**2/2; df = -2sin(x) - e**2/2
def g(x):
    return 2*(math.cos(x)) - (math.pow(math.e,x))*(0.5)

print("LETRA B")

metodoSecante(g,a,b,eps,n)

#Letra c: f = x**5 - 6 e**2/2; df = -2sin(x) - e**2/2
def h(x):
    return x**5 - 6

print("LETRA C")
metodoSecante(h,a,b,eps,n)
