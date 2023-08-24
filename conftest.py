import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book("Гордость и предубеждение и зомби")
    collector.add_new_book("Что делать, если ваш кот хочет вас убить")
    collector.add_new_book("Война и мир")
    collector.add_new_book("Капитанская дочка")
    return collector


@pytest.fixture
def collector_with_rating(collector: BooksCollector):
    collector.set_book_rating("Гордость и предубеждение и зомби", 3)
    collector.set_book_rating("Что делать, если ваш кот хочет вас убить", 8)
    collector.set_book_rating("Война и мир", 4)
    collector.set_book_rating("Капитанская дочка", 8)
    return collector


@pytest.fixture
def collector_with_favorites(collector: BooksCollector):
    collector.add_book_in_favorites("Гордость и предубеждение и зомби")
    collector.add_book_in_favorites("Что делать, если ваш кот хочет вас убить")
    collector.add_book_in_favorites("Война и мир")
    collector.add_book_in_favorites("Капитанская дочка")
    return collector
