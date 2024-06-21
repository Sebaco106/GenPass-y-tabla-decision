import unittest
from contrase import verificar_contrasena

class TestVerificarContrasena(unittest.TestCase):

    def test_longitud_superior_a_10_caracteres(self):
        resultado = verificar_contrasena("abcdefghijk")
        self.assertEqual(resultado, "La contraseña debe tener entre 8 y 10 caracteres.")

    def test_longitud_menor_a_8_caracteres(self):
        resultado = verificar_contrasena("abc123!")
        self.assertEqual(resultado, "La contraseña debe tener entre 8 y 10 caracteres.")

    def test_longitud_entre_8_y_10_caracteres(self):
        resultado = verificar_contrasena("Abcdefg1@")
        self.assertEqual(resultado, "La contraseña cumple con todos los requisitos.")

    def test_sin_letra_mayuscula(self):
        resultado = verificar_contrasena("abcdefg1!")
        self.assertEqual(resultado, "La contraseña debe contener al menos una letra mayúscula.")

    def test_sin_letra(self):
        resultado = verificar_contrasena("1234567!")
        self.assertEqual(resultado, "La contraseña debe contener al menos 2 letras.")

    def test_sin_caracter_especial(self):
        resultado = verificar_contrasena("Abcdefg1")
        self.assertEqual(resultado, "La contraseña debe contener al menos un carácter especial.")

    def test_sin_numero(self):
        resultado = verificar_contrasena("AbcdefgH!")
        self.assertEqual(resultado, "La contraseña debe contener al menos un dígito.")

    def test_sin_letra_minuscula(self):
        resultado = verificar_contrasena("ABCDEFG1!")
        self.assertEqual(resultado, "La contraseña debe contener al menos una letra minúscula.")

    def test_contrasena_valida(self):
        resultado = verificar_contrasena("Abcdefg1!")
        self.assertEqual(resultado, "La contraseña cumple con todos los requisitos.")

if __name__ == '__main__':
    unittest.main()

