from cipher.utils.helpers import str_to_index_dict
from cipher.utils.validation import validate_caesar_cipher_key, validate_caesar_alphabet


class CaesarCipher:
    """
    Класс шифрования Цезаря, который позволяет кодировать и декодировать текст
    с использованием алфавита и заданного ключа шифрования.

    Атрибуты:
        alphabet (str): Алфавит, используемый для шифрования и расшифровки.
        alphabet_dict (dict): Словарь, сопоставляющий символы алфавита их индексам.
    """

    @validate_caesar_alphabet
    def __init__(self, alphabet: str):
        """
        Инициализация класса CaesarCipher.

        Параметры:
            alphabet (str): Алфавит, который будет использоваться при шифровании и дешифровании.
        """
        self.alphabet = alphabet # Сохраняем алфавит для дальнейшего использования
        self.alphabet_dict = str_to_index_dict(alphabet) # Создаем словарь индексов символов алфавита

    @validate_caesar_cipher_key
    def encode(self, index: int, key: str, text: str):
        """
        Кодирует текст с использованием шифра Цезаря.

        Параметры:
            index (int): Индекс, из которого начинается внедрение ключа в новый алфавит.
            key (str): Ключ шифрования, который используется для создания заменяющего алфавита.
            text (str): Исходный текст для шифрования.

        Возвращает:
            str: Зашифрованный текст.
        """
        cipher_alphabet = self._create_cipher_alphabet(index, key) # Генерируем новый алфавит
        encrypted_text = ''.join(
            cipher_alphabet[self.alphabet_dict[char]] if char in self.alphabet else char
            for char in text # Применяем шифрование к каждому символу текст
        )
        return encrypted_text  # Возвращаем зашифрованный текст

    @validate_caesar_cipher_key
    def decode(self, index: int, key: str, ciphered_text: str):
        """
        Дешифрует зашифрованный текст, используя шифр Цезаря.
        """
        cipher_alphabet = self._create_cipher_alphabet(index, key) # Генерируем новый алфавит для расшифровки
        cipher_alphabet_dict = str_to_index_dict(cipher_alphabet) # Создаем словарь для зашифрованного алфавита
        decrypted_text = ''.join(
            self.alphabet[cipher_alphabet_dict[char]] if char in cipher_alphabet else char
            for char in ciphered_text # Применяем дешифрование к каждому символу зашифрованного текста
        )
        return decrypted_text # Возвращаем расшифрованный текст

    def _create_cipher_alphabet(self, index, key) -> str:
        """
        Создает шифрованный алфавит, комбинируя ключ с оставшимися символами алфавита.

        Параметры:
            index (int): Индекс, по которому будет вставлен ключ.
            key (str): Ключ шифрования, который будет добавлен в алфавит.

        Возвращает:
            str: Новый зашифрованный алфавит.
        """
        remaining_chars = ''.join([char for char in self.alphabet if char not in key]) # Получаем оставшиеся символы
        new_alphabet = remaining_chars[:index] + key + remaining_chars[index:] # Создаем новый алфавит
        return new_alphabet # Возвращаем созданный шифрованный алфавит