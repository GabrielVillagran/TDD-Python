import unittest
from calc import Calculadora

class Pruebas(unittest.TestCase):
#Test de sumas
    def test_suma_2_y_3_es_5(self):
        op = Calculadora()
        op.suma(2,3)
        self.assertEqual(5, op.valor())
    def test_suma_2_numeros_con_distinto_signo_es_resta_predomina_el_signo_del_valor_mayor(self):
        op = Calculadora()
        op.suma(-2,5)
        self.assertEqual(3, op.valor())
    def test_suma_2_numeros_negativos_es_incremento_negativo(self):
        op = Calculadora()
        op.suma(-2,-3)
        self.assertEqual(-5, op.valor())
#test resta
    def test_resta_2_y_1_es_1(self):
        op = Calculadora()
        op.resta(2,1)
        self.assertEqual(1, op.valor())
    def test_resta_2_numeros_negativos_es_decremento_positivo(self):
        op = Calculadora()
        op.resta(-2,-5)
        self.assertEqual(3, op.valor())
    def test_resta_positivo_y_negativo_es_suma_negativa(self):
        op = Calculadora()
        op.resta(-2,7)
        self.assertEqual(-9, op.valor())
#test multiplicacion
    def test_multiplicacion_2_y_1_es_2(self):
        op = Calculadora()
        op.multiplicacion(2,1)
        self.assertEqual(2, op.valor())
    def test_multiplicacion_2_numeros_negativos_es_positivo(self):
        op = Calculadora()
        op.multiplicacion(-2,-2)
        self.assertEqual(4, op.valor())
    def test_multiplicacion_un_numero_negativo_y_positivo_es_negativo(self):
        op = Calculadora()
        op.multiplicacion(-2,2)
        self.assertEqual(-4, op.valor())
#test division
    def test_division_4_y_2_es_2(self):
        op = Calculadora()
        op.division(4,2)
        self.assertEqual(2, op.valor())
    def test_division_negativo_y_megativo_es_positivo(self):
        op = Calculadora()
        op.division(-4,-2)
        self.assertEqual(2, op.valor())
    def test_division_negativo_y_positivo_es_negativo(self):
        op = Calculadora()
        op.division(-4,2)
        self.assertEqual(-2, op.valor())
#test exponente
    def test_2_al_cuadrado_es_4(self):
        op = Calculadora()
        op.exp(2,2)
        self.assertEqual(4, op.valor())   
    def test_numeros_negativos_al_cuadrado_es_positivo(self):
        op = Calculadora()
        op.exp(-2,2)
        self.assertEqual(4, op.valor())  
    def test_numeros_negativos_al_exponente_impar_es_negativo(self):
        op = Calculadora()
        op.exp(-2,3)
        print("")
        self.assertEqual(-8, op.valor())   
#test cuadratica
    def test_2_al_cuadrado_es_4(self):
        op = Calculadora()
        op.cuadratica(1,-5,6)
        self.assertEqual(3, op.valor())  