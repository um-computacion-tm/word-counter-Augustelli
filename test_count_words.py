import unittest

from count_words import count_words


class TestCountWords(unittest.TestCase):

    def test_01(self):
        resultado = count_words('a')
        resultado_esperado = {'a': 1}
        self.assertEqual(resultado_esperado, resultado)

    def test_02(self) : 
        resultado = count_words('hola mundo')
        resultado_esperado = {
            
            'hola' :1,
            'mundo' : 1                   
        }
        self.assertEqual(resultado_esperado, resultado)
        
    def test_03(self):
        resultado = count_words('Holaa holaa como CoMMO')
        resultado_esperado = {
            'holaa' : 2 ,
            'como' : 1,
            'commo' : 1,

        }
        self.assertEquals(resultado_esperado, resultado)
    
    def test_04(self):
        resultado = count_words('')
        resultado_esperado = {
            
        }
        self.assertEquals(resultado_esperado, resultado)

    def test_05(self):
        resultado = count_words('   asd   ')
        resultado_esperado = {
            'asd' : 1.
        }
        self.assertEquals(resultado_esperado, resultado)



if __name__ == '__main__':
    unittest.main()