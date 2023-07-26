import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("rating", [3, 10])
    def test_set_book_rating_assigned_rating_rating_set(
        self, rating, collector: BooksCollector
    ):
        collector.set_book_rating("Гордость и предубеждение и зомби", rating)
        assert collector.get_book_rating("Гордость и предубеждение и зомби") == rating

    @pytest.mark.parametrize("rating", [-1, 13])
    def test_set_book_rating_assigned_rating_rating_not_set(
        self, rating, collector: BooksCollector
    ):
        collector.set_book_rating("Гордость и предубеждение и зомби", rating)
        assert collector.get_book_rating("Гордость и предубеждение и зомби") != rating

    @pytest.mark.parametrize(
        "book, rating",
        [("Гордость и предубеждение и зомби", 3), ("Капитанская дочка", 8)],
    )
    def test_get_book_rating_book_and_expected_rating_rating_received(
        self, book, rating, collector_with_rating: BooksCollector
    ):
        assert collector_with_rating.get_book_rating(book) == rating

    def test_get_books_with_specific_rating_books_received(
        self, collector_with_rating: BooksCollector
    ):
        assert [
            "Что делать, если ваш кот хочет вас убить",
            "Капитанская дочка",
        ] == collector_with_rating.get_books_with_specific_rating(8)

    def test_get_books_rating_books_received(self):
        books = ["Война и мир", "Капитанская дочка"]
        collector = BooksCollector()
        for book in books:
            collector.add_new_book(book)
        assert list(collector.get_books_rating().keys()) == books

    @pytest.mark.parametrize("book", ["Война и мир", "Капитанская дочка"])
    def test_add_book_in_favorites_added_book_favorite_book(
        self, book, collector: BooksCollector
    ):
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
        "book", ["Война и мир", "Что делать, если ваш кот хочет вас убить"]
    )
    def test_delete_book_from_favorites_deleted_book_book_not_favorites(
        self, book, collector_with_favorites: BooksCollector
    ):
        collector_with_favorites.delete_book_from_favorites(book)
        assert book not in collector_with_favorites.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_favorites_received(
        self, collector: BooksCollector
    ):
        books = ["Война и мир", "Капитанская дочка"]
        for book in books:
            collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == books

    def test_get_book_rating_rating_new_book_one(self, collector: BooksCollector):
        assert collector.get_book_rating("Война и мир") == 1
