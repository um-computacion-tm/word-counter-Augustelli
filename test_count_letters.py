import unittest

from count_letters import count_letters

class TestCountLetters(unittest.TestCase):

    def test_01(self):
        resultado = count_letters('a')
        resultado_esperado = {'a' : 1}
        self.assertEqual(resultado_esperado, resultado)


    def test_02(self) : 
        resultado = count_letters('hola')
        resultado_esperado = {
            
            'h': 1,
            'o' : 1,
            'l' : 1,
            'a' : 1                   
        }
        self.assertEqual(resultado_esperado, resultado)


    def test_03(self) : 
        resultado = count_letters('')
        resultado_esperado = {
                            
        }
        self.assertEqual(resultado_esperado, resultado)


    def test_04(self) : 
        resultado = count_letters('AaaHhlha')
        resultado_esperado = {
            
            'h': 3,
            'a' : 4,
            'l' : 1                   
        }
        self.assertEqual(resultado_esperado, resultado)


    def test_05(self) : 
        resultado = count_letters('holaasdA ')
        resultado_esperado = {
               'h' : 1,
               'o' : 1,
               'l' : 1,
               'a' : 3,
               's' : 1,
               'd' : 1,
               ' ' : 1, 
        }
        self.assertEqual(resultado_esperado, resultado)

if __name__ == '__main__':
    unittest.main()