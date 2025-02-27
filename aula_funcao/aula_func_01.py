def multiplica(*args):
    contador = 1
    for i in args:
        contador *= i
    return contador
    

m = multiplica(1, 2, 3, 4, 5)

def par(n):
    multiplo_dois = n %2 == 0
    if multiplo_dois:
        return f'{n} é par'
    return f'{n} é ímpar'


p = par(22)


print(m)
print(p)