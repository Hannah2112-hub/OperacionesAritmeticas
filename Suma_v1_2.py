#Orientado a objetos
class OperacionesAritmeticas:
    def ingresoNumeros(self):
        numero1 = float(input("Ingrese el primer sumando: "))
        numero2 = float(input("Ingrese el segundo sumando: "))
        return numero1,numero2
    def suma(numero1,numero2):
        return numero1+numero2

if __name__ == '__main__':
    operación = OperacionesAritmeticas()
    num1,num2=operación.ingresoNumeros()
    print(f"{num1}+{num2}={operación.suma(num1, num2)}")