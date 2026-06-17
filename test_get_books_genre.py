class TestGetBooksGenre:
# 1. Возвращается пустой словарь после создания объекта
    def test_get_books_genre_returns_empty_dict(collector):
        assert collector.get_books_genre() == {}

# 2. Возвращается словарь с одной книгой
    def test_get_books_genre_returns_one_book(collector):
        collector.books_genre = {'Дюна': 'Фантастика'}
        assert collector.get_books_genre() == {
            'Дюна': 'Фантастика'
        }

# 3. Возвращается словарь с несколькими книгами
    def test_get_books_genre_returns_multiple_books(collector):
        collector.books_genre = {
            'Дюна': 'Фантастика',
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы'
        }

        assert collector.get_books_genre() == {
            'Дюна': 'Фантастика',
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы'
        }


# 4. Метод возвращает объект типа dict
    def test_get_books_genre_returns_dict_type(collector):
        assert isinstance(collector.get_books_genre(), dict)

# 5. Проверка количества элементов
    def test_get_books_genre_returns_correct_length(collector):
        collector.books_genre = {
            'Дюна': 'Фантастика',
            'Оно': 'Ужасы'
        }
        assert len(collector.get_books_genre()) == 2

# 6. Проверка наличия книги в результате
    def test_get_books_genre_contains_book(collector):
        collector.books_genre = {'Дюна': 'Фантастика'}
        assert 'Дюна' in collector.get_books_genre()


# 7. Проверка жанра конкретной книги
    def test_get_books_genre_returns_correct_genre(collector):
        collector.books_genre = {'Оно': 'Ужасы'}
        assert collector.get_books_genre()['Оно'] == 'Ужасы'

# 8. Проверка отсутствия несуществующей книги
    def test_get_books_genre_not_contains_unknown_book(collector):
        collector.books_genre = {'Дюна': 'Фантастика'}
        assert 'Гарри Поттер' not in collector.get_books_genre()

# 9. Метод возвращает актуальное содержимое словаря
    def test_get_books_genre_returns_actual_data(collector):
        collector.books_genre['Дюна'] = 'Фантастика'
        result = collector.get_books_genre()
        assert result == {'Дюна': 'Фантастика'}
