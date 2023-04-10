import unittest
from contadordepalabrasfrancoquiroga import contadorpalabra

class Testclase3comp(unittest.TestCase):
    def test_hola(self):
        resultado = contadorpalabra('hola')
        self.assertEqual(resultado, {'hola':1})
    def test_hola_(self):
        resultado = contadorpalabra('hola_')
        self.assertEqual(resultado, {'hola':1})
    def test_hola_(self):
        resultado = contadorpalabra('hola HOla CHAU chau')
        self.assertEqual(resultado, {'hola':2, 'chau':2} )
    def test_SeParar_test_de_los_programas_TEST(self):
        resultado = contadorpalabra('SeParar test de los programas TEST')
        self.assertEqual(resultado, {'test':2, 'separar':1, 'de':1,'los':1, 'programas':1} )
    def test_el_problema_esta_mal_planteado(self):
        resultado = contadorpalabra('el problema esta mal planteado')
        self.assertEqual(resultado, {'el':1, 'problema':1, 'esta':1,'mal':1, 'planteado':1} )
    def test_este_test_DEBERIA_andar_bien(self):
        resultado = contadorpalabra('este test DEBERIA andar bien   ')
        self.assertEqual(resultado, {'este':1, 'test':1, 'deberia':1,'andar':1, 'bien':1} )
    def test_NO_No_nO_no_SI_SI_SI_SI(self):
        resultado = contadorpalabra('NO No nO no SI SI SI SI')
        self.assertEqual(resultado, {'no':4, 'si':4} )


if __name__ == '__main__':
    unittest.main()
