p = int(input("precio por unidad: "))
f = int(input("costo fijo: "))
v = int(input("costo variable: "))
u = int(input("número de unidades vendidas: "))

ganancia = p*u-(f+v*u)
equilibrio = f/(p-v)
print("punto de equilibrio : ", equilibrio)
print("ganancia : ", ganancia)
