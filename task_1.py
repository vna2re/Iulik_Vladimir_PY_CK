# TODO Написать 3 класса с документацией и аннотацией типов

class Book:
    """
     Класс, представляющий книгу.

    Атрибуты:
        author (str): Автор книги.
        pages (int): Общее количество страниц.
        read_pages (int): Количество прочитанных страниц.
    """
    def __init__(self, author: str, pages: int, read_pages: int = 0):
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages
        self.author = author
        self.read_pages = read_pages

    def increment_last_read_page(self, additional_pages: int):
        """
        Увеличивает количество прочитанных страниц.

        Аргументы:
            additional_pages (int): Количество страниц, которые были прочитаны дополнительно.

        Ошибки:
            ValueError: Если дополнительное количество страниц отрицательное или превышает оставшиеся страницы.
        """
        if not isinstance(additional_pages, int):
            raise TypeError("Прочитанные страницы должны быть типа int")
        if additional_pages < 0:
            raise ValueError("Прочитанные страницы должны быть положительным числом")
        if self.read_pages + additional_pages > self.pages:
            raise ValueError("Количество прочитанных страниц не может превышать общее количество страниц")
        self.read_pages += additional_pages


class Library:
    """
    Класс, представляющий библиотеку.

    Атрибуты:
        name (str): Название библиотеки.
        books (List[Book]): Список книг в библиотеке.
    """
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Название библиотеки должно быть строкой")
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        """
        Добавляет книгу в библиотеку.

        Аргументы:
            book (Book): Объект книги для добавления.
        """
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты класса Book")
        self.books.append(book)

    def get_books_by_author(self, author: str) -> list[Book]:
        """
        Возвращает список книг указанного автора.

        Аргументы:
            author (str): Имя автора.

        Возвращает:
            List[Book]: Список книг автора.
        """
        return [book for book in self.books if book.author == author]


class Reader:
    """
    Класс, представляющий читателя.

    Атрибуты:
        name (str): Имя читателя.
        books_read (List[Book]): Список книг, которые читатель прочитал.
    """
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Имя читателя должно быть строкой")
        self.name = name
        self.books_read = []

    def add_book_to_read(self, book: Book):
        """
        Добавляет книгу в список прочитанных.

        Аргументы:
            book (Book): Объект книги.

        Ошибки:
            ValueError: Если книга не полностью прочитана.
        """
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты класса Book")
        if book.read_pages < book.pages:
            raise ValueError("Нельзя добавить непрочитанную книгу")
        self.books_read.append(book)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
