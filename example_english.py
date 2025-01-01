from cipher.caesar_cipher import CaesarCipher
import random


def main():
    """
    Основная функция программы, демонстрирующая шифрование и дешифрование текста с использованием
    шифра Цезаря.

    В этой функции:
    - Инициализируется алфавит для шифрования.
    - Шифруется заданный текст с помощью ключа и индекса.
    - Далее происходит дешифрование зашифрованного текста, чтобы подтвердить корректность работы.
    """
    # Определяем английский алфавит, который будет использован в шифре
    eng_alphabet = "abcdefghijklmnopqrstuvwxyz "
    # Инициализируем объект шифра Цезаря с указанным алфавитом
    caesar_cipher_eng = CaesarCipher(eng_alphabet)

    # Исходный текст, который мы будем шифровать
    text = "A journey of a thousand miles begins with a single step"
    print(f"Original text is '{text}'")
    # Индекс сдвига для шифра Цезаря
    index = random.randint(0, len(eng_alphabet))
    # Ключ, который будет использоваться для шифрования
    key = "diplomat"
    # Кодируем текст с использованием указанного индекса и ключа
    encoded_text = caesar_cipher_eng.encode(index, key, text)
    print(f"Encoded text is '{encoded_text}'")

    # Дешифруем зашифрованный текст, чтобы проверить правильность
    decoded_text = caesar_cipher_eng.decode(index, key, encoded_text)
    print(f"Decoded text is '{decoded_text}'")


if __name__ == "__main__":
    main()