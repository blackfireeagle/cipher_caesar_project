from cipher.exceptions import InvalidCipherKeyException, InvalidCipherIndexException


def validate_caesar_cipher_key(method):
    """
    Декоратор для валидации ключа шифра Цезаря перед вызовом метода.

    Проверяет:
    - Длину ключа
    - Наличие дубликатов в ключе
    - Наличие недопустимых символов в ключе
    """
    def wrapper(self, index: int, key: str, text: str):
        # Проверка на превышение длины ключа
        if len(key) > len(self.alphabet):
            raise InvalidCipherKeyException(
                f"Length of key ({len(key)}) can't be greater than alphabet length ({len(self.alphabet)})."
            )
        # Проверка на наличие дубликатов в ключе
        if len(set(key)) != len(key):
            raise InvalidCipherKeyException(
                f"Key can't contain same letter multiple times."
            )
        # Проверка на наличие недопустимых символов в ключе
        if not set(key).issubset(set(key)):
            raise InvalidCipherKeyException(
                f"Key can't contain characters that are not in the alphabet."
            )

        return method(self, index, key, text)

    return wrapper


def validate_caesar_alphabet(method):
    """
    Декоратор для валидации алфавита перед вызовом метода.

    Проверяет, что в алфавите отсутствуют дубликаты.
    """
    def wrapper(self, alphabet: str):
        # Проверка на наличие дубликатов в алфавите
        if len(set(alphabet)) != len(alphabet):
            raise InvalidCipherKeyException(
                f"Alphabet can't contain same letter multiple times."
            )
        return method(self, alphabet)
    return wrapper