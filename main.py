class Book:
    """Базовый класс книги с неизменяемыми атрибутами name и author.

    Атрибуты:
        _name (str): Название книги (приватное, доступно только для чтения через свойство name).
        _author (str): Автор книги (приватное, доступно только для чтения через свойство author).
    """
    def __init__(self, name: str, author: str):
        """
        Инициализация объекта Book.

        Аргументы:
            name (str): Название книги.
            author (str): Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """
        str: Название книги, доступно только для чтения.
        """
        return self._name

    @property
    def author(self) -> str:
        """
        str: Автор книги, доступно только для чтения.
        """
        return self._author

    def __str__(self):
        """
        Возвращает строковое представление книги.

        Возвращает:
            str: Строка будет такой "Книга {name}. Автор {author}".
        """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """
        Возвращает подробное строковое представление объекта книги.

        Возвращает:
            str: Строка будет "Book(name=<name>, author=<author>)", где <name> и <author> — значения соответствующих атрибутов.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Класс для бумажной книги, наследуется от Book.

    Атрибуты:
        _pages (int): Количество страниц в книге (приватное, доступно только для чтения через свойство pages).
    """
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация объекта PaperBook.

        Аргументы:
            name (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц.

        Ошибки при проверках:
            TypeError: Если pages не является целым числом.
            ValueError: Если pages не является положительным числом.
        """
        super().__init__(name, author)
        # Проверка параметра pages в бумажной книжке
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    @property
    def pages(self) -> int:
        """
        int: Количество страниц, доступно только для чтения.
        """
        return self._pages

    def __repr__(self):
        """
        Возвращает подробное строковое представление бумажной книги.

        Возвращает:
            str: Строка будет такой "PaperBook(name=<name>, author=<author>, pages=<pages>)".
        """
        base_repr = super().__repr__()[:-1]
        return f"{base_repr}, pages={self.pages})"


class AudioBook(Book):
    """
    Класс для аудиокниги, наследуется от Book.

    Атрибуты:
        _duration (float): Продолжительность аудиокниги (приватное, доступно только для чтения через свойство duration).
    """
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация объекта AudioBook.

        Аргументы:
            name (str): Название книги.
            author (str): Автор книги.
            duration (float): Продолжительность аудиокниги.

        Ошибки:
            TypeError: Если duration не является числом.
            ValueError: Если duration не является положительным числом.
        """
        super().__init__(name, author)
        # Проверка параметра duration в удио книжке
        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжительность аудио должна быть числом")
        if duration <= 0:
            raise ValueError("Продолжительность аудио должна быть положительным числом")
        self._duration = duration

    @property
    def duration(self) -> float:
        """
        float: Продолжительность аудиокниги, доступно только для чтения.
        """
        return self._duration

    def __repr__(self):
        """
        Возвращает подробное строковое представление аудиокниги.

        Возвращает:
            str: Строка будет такой "AudioBook(name=<name>, author=<author>, duration=<duration>)".
        """
        base_repr = super().__repr__()[:-1]
        return f"{base_repr}, duration={self.duration})"


# Пример использования:
if __name__ == "__main__":
    pb = PaperBook("Война и мир", "Лев Толстой", 100)
    ab = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 999.1)

    print(repr(pb))
    print(repr(ab))

    # Пробуем изменить число страниц
    try:
        pb.pages = 1200
    except AttributeError as e:
        print(e)  # Это вывод ошибки, что мы не смогли поменять число страниц.
    print(repr(pb))  # Смотрим, что страницы действительно не поменялись

    # Пробуем изменить продолжительность страниц
    try:
        ab.duration = 20
    except AttributeError as e:
        print(e)  # Это вывод ошибки, что мы не смогли поменять продолжительность.
    print(repr(ab))  # Смотрим, что продолжительность действительно не поменялась