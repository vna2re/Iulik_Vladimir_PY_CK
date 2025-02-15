class Book:
    """
    Базовый класс книги с атрибутами title, author, year, genre.

    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        genre (str): Жанр книги.
    """

    def __init__(self, title: str, author: str, year: int, genre: str) -> None:
        """
        Инициализация книги с названием, автором, годом издания и жанром.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            genre (str): Жанр книги.
        """
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_age(self, current_year: int) -> int:
        """
        Возвращает возраст книги в годах.

        Аргументы:
            current_year (int): Текущий год.

        Возвращает:
            int: Возраст книги в годах.
        """
        return current_year - self.year

    def get_description(self) -> str:
        """
        Описание книги.

        Возвращает:
            str: Строковое описание книги.
        """
        return f"{self.title} — книга жанра {self.genre}, написанная {self.author} в {self.year} году."

    def __str__(self) -> str:
        """
        Строковое представление объекта книги.

        Возвращает:
            str: Строковое представление книги.
        """
        return f"'{self.title}' by {self.author} ({self.year}), Genre: {self.genre}"

    def __repr__(self) -> str:
        """
        Представление книги для отладки.

        Возвращает:
            str: Строковое представление книги для отладки.
        """
        return (f"Book(title='{self.title}', author='{self.author}', "
                f"year={self.year}, genre='{self.genre}')")


class EBook(Book):
    """
    Класс электронной книги, наследуемый от класса Book, с дополнительными атрибутами для формата и размера файла.

    Атрибуты:
        file_format (str): Формат электронной книги (например, PDF).
        file_size (float): Размер файла в МБ.
        drm_protected (bool): Указывает, защищена ли книга от копирования.
    """

    def __init__(self, title: str, author: str, year: int, genre: str,
                 file_format: str, file_size: float, drm_protected: bool) -> None:
        """
        Инициализация электронной книги с дополнительными атрибутами.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            genre (str): Жанр книги.
            file_format (str): Формат электронной книги (например, PDF).
            file_size (float): Размер файла в МБ.
            drm_protected (bool): Указывает, защищена ли книга от копирования.
        """
        super().__init__(title, author, year, genre)
        self.file_format = file_format
        self.file_size = file_size
        self.drm_protected = drm_protected

    def download(self) -> str:
        """
        Имитация скачивания электронной книги.

        Возвращает:
            str: Сообщение о процессе скачивания.
        """
        return f"Downloading '{self.title}' in {self.file_format} format... Done!"

    def get_description(self) -> str:
        """
        Перегруженный метод для получения описания электронной книги с дополнительными атрибутами.

        Возвращает:
            str: Описание электронной книги.
        """
        drm_info = "с защитой DRM" if self.drm_protected else "без защиты DRM"
        return (f"{super().get_description()} Это электронная версия в формате {self.file_format}, "
                f"размером {self.file_size}MB, {drm_info}.")

    def __str__(self) -> str:
        """
        Строковое представление объекта электронной книги.

        Возвращает:
            str: Строковое представление электронной книги.
        """
        drm_info = "Protected" if self.drm_protected else "Not Protected"
        return (super().__str__() +
                f" [E-Book: {self.file_format}, {self.file_size}MB, DRM: {drm_info}]")

    def __repr__(self) -> str:
        """
        Представление электронной книги для отладки.

        Возвращает:
            str: Строковое представление электронной книги для отладки.
        """
        return (f"EBook(title='{self.title}', author='{self.author}', year={self.year}, "
                f"genre='{self.genre}', file_format='{self.file_format}', "
                f"file_size={self.file_size}, drm_protected={self.drm_protected})")


class PaperBook(Book):
    """
    Класс бумажной книги, наследуемый от класса Book, с дополнительными атрибутами для физических характеристик.

    Атрибуты:
        __pages (int): Количество страниц в книге (непубличное).
        cover_type (str): Тип обложки (твердая или мягкая).
        is_signed (bool): Указывает, подписана ли книга автором.
    """

    def __init__(self, title: str, author: str, year: int, genre: str,
                 pages: int, cover_type: str, is_signed: bool) -> None:
        """
        Инициализация бумажной книги с дополнительными атрибутами.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            genre (str): Жанр книги.
            pages (int): Количество страниц в книге.
            cover_type (str): Тип обложки (твердая или мягкая).
            is_signed (bool): Указывает, подписана ли книга автором.
        """
        super().__init__(title, author, year, genre)
        self.__pages = pages  #Количество страниц в книге (непубличное).
        self.cover_type = cover_type
        self.is_signed = is_signed

    def get_pages(self) -> int:
        """
        Геттер для атрибута pages.

        Возвращает:
            int: Количество страниц в книге.
        """
        return self.__pages

    def set_pages(self, pages: int) -> None:
        """
        Сеттер для атрибута pages.

        Аргументы:
            pages (int): Количество страниц в книге.

        Исключения:
            ValueError: Если количество страниц не положительное.
        """
        if pages > 0:
            self.__pages = pages
        else:
            raise ValueError("Количество страниц должно быть положительным числом.")

    def open_page(self, page: int) -> str:
        """
        Имитация открытия страницы книги.

        Аргументы:
            page (int): Номер страницы для открытия.

        Возвращает:
            str: Сообщение об открытии страницы или ошибке.
        """
        if 1 <= page <= self.__pages:
            return f"Opening page {page} of '{self.title}'"
        else:
            return f"Error: '{self.title}' has only {self.__pages} pages."

    def get_description(self) -> str:
        """
        Перегруженный метод для получения описания бумажной книги с дополнительными атрибутами.

        Возвращает:
            str: Описание бумажной книги.
        """
        signed_info = "с автографом автора" if self.is_signed else "без автографа"
        return (f"{super().get_description()} Это бумажная книга на {self.__pages} страниц, "
                f"в {self.cover_type} переплете, {signed_info}.")

    def __str__(self) -> str:
        """
        Строковое представление объекта бумажной книги.

        Возвращает:
            str: Строковое представление бумажной книги.
        """
        signed_info = "Signed" if self.is_signed else "Not Signed"
        return (super().__str__() +
                f" [Paper Book: {self.__pages} pages, {self.cover_type} cover, {signed_info}]")

    def __repr__(self) -> str:
        """
        Представление бумажной книги для отладки.

        Возвращает:
            str: Строковое представление бумажной книги для отладки.
        """
        return (f"PaperBook(title='{self.title}', author='{self.author}', year={self.year}, "
                f"genre='{self.genre}', pages={self.__pages}, cover_type='{self.cover_type}', "
                f"is_signed={self.is_signed})")


if __name__ == "__main__":
    # Создание объектов
    ebook = EBook("1984", "George Orwell", 1949, "Dystopia", "PDF", 1.5, True)
    paperbook = PaperBook("To Kill a Mockingbird", "Harper Lee", 1960, "Novel", 281, "hardcover", False)

    # Перегруженные методы
    print(ebook.get_description())  # Перегруженный метод для электронной книги
    print(paperbook.get_description())  # Перегруженный метод для бумажной книги

    # Унаследованные методы
    print(f"'{ebook.title}' age: {ebook.get_age(2025)} years")  # Унаследованный метод
    print(f"'{paperbook.title}' age: {paperbook.get_age(2025)} years")  # Унаследованный метод

    # Строковые представления
    print(ebook)  # __str__
    print(repr(ebook))  # __repr__
    print(paperbook)  # __str__
    print(repr(paperbook))  # __repr__

    # Пример использования геттеров и сеттеров
    print(paperbook.get_pages())  # Получить количество страниц
    paperbook.set_pages(300)  # Установить количество страниц
    print(paperbook.get_pages())  # Проверить новое количество страниц
