class TestGetBookGenre:
#1. Проверка возврата жанра «Фантастика»
    def test_get_book_genre_returns_fantasy(collector):
        collector.books_genre['Дюна'] = 'Фантастика'
        assert collector.get_book_genre('Дюна') == 'Фантастика'

#2. Проверка возврата жанра «Ужасы»
    def test_get_book_genre_returns_horror(collector):
        collector.books_genre['Оно'] = 'Ужасы'
        assert collector.get_book_genre('Оно') == 'Ужасы'

#3. Проверка возврата жанра «Детективы»
    def test_get_book_genre_returns_detective(collector):
        collector.books_genre['Шерлок Холмс'] = 'Детективы'
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

#4. Проверка возврата жанра «Мультфильмы»
    def test_get_book_genre_returns_cartoon(collector):
        collector.books_genre['Король Лев'] = 'Мультфильмы'
        assert collector.get_book_genre('Король Лев') == 'Мультфильмы'

#5. Проверка возврата жанра «Комедии»
    def test_get_book_genre_returns_comedy(collector):
        collector.books_genre['Трое в лодке'] = 'Комедии'
        assert collector.get_book_genre('Трое в лодке') == 'Комедии'

#6. Проверка возврата None для отсутствующей книги
    def test_get_book_genre_returns_none_for_unknown_book(collector):
        assert collector.get_book_genre('Неизвестная книга') is None

#7. Возврат None при пустом словаре.
    def test_get_book_genre_returns_none_when_dictionary_empty(collector):
        assert collector.get_book_genre('Дюна') is None

#8. Провекра корректного поиска среди нескольких книг
    def test_get_book_genre_returns_correct_genre_among_many_books(collector):
        collector.books_genre = {
            'Дюна': 'Фантастика',
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы'
        }
        assert collector.get_book_genre('Оно') == 'Ужасы'

#9. Проверка чувствительности поиска к регистру
    def test_get_book_genre_is_case_sensitive(collector):
        collector.books_genre['Дюна'] = 'Фантастика'
        assert collector.get_book_genre('дюна') is None
