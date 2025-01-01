class InvalidCipherKeyException(Exception):
    """
    Исключение, которое возникает, когда ключ шифрования недействителен.
    Например, если его длина больше длины алфавита или если он содержит
    повторы символов.
    """
    def __init__(self, message: str):
        """
        Инициализирует исключение InvalidCipherKeyException.
        """
        super().__init__(message)


class InvalidCipherIndexException(Exception):
    """
    Исключение, которое возникает, когда индекс для шифрования недействителен.
    Например, если индекс превышает допустимый диапазон алфавита.
    """
    def __init__(self, message: str):
        """
        Инициализирует исключение InvalidCipherIndexException.
        """
        super().__init__(message)


class InvalidAlphabet(Exception):
    """
    Исключение, которое возникает, когда задан недопустимый алфавит.
    Например, если алфавит пуст или содержит недопустимые символы.
    """
    def __init__(self, message):
        """
        Инициализирует исключение InvalidAlphabet.
        """
        super().__init__(message)