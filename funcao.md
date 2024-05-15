```
len
int
float
type
print
input

define funcao com:
    def nome(1, 2, 3)
        codigo
        return
----------------------------
n = 5
i = 1
while i <= n:
    print(i, end='\n')
    i += 1
---------------------------------------------

n = 5
# Execução para j = 1
i = 1
j = 1

while i <= j:
    print(i, end=' ')
    i += 1
# --------- j = 2 ------------
print()

i = 1
j = 2

while i <= j:
    print(i, end=' ')
    i += 1

print()

i = 1
j = 3

while i <= j:
    print(i, end=' ')
    i += 1

====================================================================



n = 5
i = 1
j = 1

while j <= n:
    i = 1
    while i <= j:
        print(i, end=' ')
        i += 1
    print()
    j+=1



=======================================================================


EM FUNÇÃO:

def imprime_tela(n):

    n = 5
    i = 1

    j = 1
    while j <= n:
        i = 1
        while i <= j:
            print(i, end=' ')
            i += 1
        print()
        j += 1
    return None

imprime_tela(10)



=======================================================================

def mult(a, b):
    c = a - b
    return c

print(mult(3, 1))

=======================================================================

def eq_segundo_grau(a, b, c):

    delta = b**2 - 4*a*c
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)
    return x1, x2

print(eq_segundo_grau(1, -6, 8))




```
