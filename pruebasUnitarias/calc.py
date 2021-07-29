from math import sqrt
class Calculadora:
    total = 0
    def valor(self):
        return self.total
#suma    
    def suma(self, num1, num2):
        print("====== Suma ======")
        print(num1, "+", num2, "=", num1 + num2)
        print("==================")
        self.total = num1 + num2
#resta  
    def resta(self, num1, num2):
        print("====== Resta ======")
        print(num1, "-", num2, "=", num1 - num2)
        print("==================")
        self.total = num1 - num2
#multiplicacion  
    def multiplicacion(self, num1, num2):
        print("====== Multiplicacion ======")
        print(num1, "*", num2, "=", num1 * num2)
        print("==================")
        self.total = num1 * num2
#Division 
    def division(self, num1, num2):
        print("====== Division ======")
        try:
            print(num1, "/", num2, "=", num1 / num2)
            self.total = num1 / num2
            print("==================")
        except ZeroDivisionError:
            print("MATH ERROR")
            print("==================")
#Exponente  
    def exp(self, num1, num2):
        print("====== Exponente ======")
        print(num1, "^", num2, "=", pow(num1, num2))
        self.total = pow(num1, num2)
        print("==================")
#Cuadratica  
    def cuadratica(self, A, B, C):
        print("====== Cuadratica ======")
        if ((B**2)-4*A*C) < 0:
            print("La solución de la ecuación es con numeros complejos")
        else:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte positiva
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)  # Fórmula de Bhaskara parte negativa
            self.total = x1
            #self.total = x2
            print("Las soluciones de la ecuación son:")
            print("x1 = ", x1)
            print("x2 = ", x2)