"""Реализуйте класс CaesarCipher для шифровки и дешифровки текста с помощью шифра Цезаря. При создании экземпляра класса CaesarCipher должен указываться сдвиг, который будет использоваться при шифровке и дешифровке. За операцию шифрования должен отвечать метод encode(), за операцию дешифрования — decode():

cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek
Обратите внимание, что при шифровке сдвиг должен происходить вправо, также заметьте, что регистр букв при шифровке и дешифровке должен сохраняться.

Шифровке и дешифровке должны подвергаться только буквы латинского алфавита, все остальные символы, если они присутствуют, должны оставаться неизменными:

print(cipher.encode('Биgeek123'))    # Биljjp123
print(cipher.decode('Биljjp123'))    # Биgeek123
Примечание 1. Гарантируется, что сдвигом является число из диапазона [1; 26]."""


class CaesarCipher():
    alpha = {
        **{chr(num): num for num in range(ord('A'), ord('Z') + 1)},
        **{chr(num): num for num in range(ord('a'), ord('z') + 1)},
           }

    reversed_alpha = {value: key for key, value in alpha.items()}

    def __init__(self, shift):
        self.shift = shift

    @staticmethod
    def code(shift, string:str):
        new_string = [chr((CaesarCipher.alpha[item] - (variable:= (
            ord('A') if item.isupper() else ord('a'))) + shift) % 26 + variable) if item in CaesarCipher.alpha else item for item in
                      string]
        return "".join(new_string)

    def encode(self, string: str):
        return CaesarCipher.code(self.shift, string)

    def decode(self,string: str):
        return CaesarCipher.code(-self.shift, string)

cipher = CaesarCipher(-1)

print(cipher.encode('a'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek