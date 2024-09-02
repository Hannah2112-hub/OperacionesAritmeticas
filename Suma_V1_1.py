def ingresoNumeros():
    numero1 = float(input("Ingrese el primer sumando: "))
    numero2 = float(input("Ingrese el segundo sumando: "))
    return numero1,numero2
def suma(numero1,numero2):
    return numero1+numero2

if __name__ == '__main__'_
num1,num2=ingresoNumeros()
print(f"{num1}+{num2}={suma(num1, num2)}")