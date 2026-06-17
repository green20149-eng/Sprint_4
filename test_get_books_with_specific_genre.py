class TestGetBooks:
    def test_get_books_with_specific_genre_returns_empty_list_when_no_books(collector):
    #1. Проверка, что при отсутствии книг метод возвращает пустой список
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_returns_one_fantasy_book(collector):
    #2. Проверка возврата одной книги жанра "Фантастика"
        collector.books_genre = {
            'Дюна': 'Фантастика'
        }
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    def test_get_books_with_specific_genre_returns_several_fantasy_books(collector):
    #3. Проверка возврата нескольких книг одного жанра
        collector.books_genre = {
           'Дюна': 'Фантастика',
            'Основание': 'Фантастика',
            'Оно': 'Ужасы'
        }
        assert collector.get_books_with_specific_genre('Фантастика') == [
            'Дюна',
            'Основание'
        ]

    def test_get_books_with_specific_genre_returns_horror_books(collector):
    #4. Проверка возврата книг жанра "Ужасы"
        collector.books_genre = {
            'Оно': 'Ужасы',
            'Кладбище домашних животных': 'Ужасы',
            'Дюна': 'Фантастика'
        }

        assert collector.get_books_with_specific_genre('Ужасы') == [
            'Оно',
            'Кладбище домашних животных'
        ]

    def test_get_books_with_specific_genre_returns_empty_list_for_unknown_genre(collector):
    #5. Проверка возврата пустого списка для жанра, которого нет в списке допустимых
        collector.books_genre = {
            'Дюна': 'Фантастика'
        }
        assert collector.get_books_with_specific_genre('Роман') == []


    def test_get_books_with_specific_genre_returns_empty_list_when_genre_has_no_books(collector):
    #6. Проверка возврата пустого списка, если книг указанного жанра нет
        collector.books_genre = {
            'Дюна': 'Фантастика',
            'Оно': 'Ужасы'
        }
        assert collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_with_specific_genre_preserves_books_order(collector):
    #7. Проверка сохранения порядка книг в результате
        collector.books_genre = {
            'Книга 1': 'Детективы',
            'Книга 2': 'Детективы',
            'Книга 3': 'Детективы'
        }

        assert collector.get_books_with_specific_genre('Детективы') == [
            'Книга 1',
            'Книга 2',
            'Книга 3'
        ]

    def test_get_books_with_specific_genre_returns_list_type(collector):
    #8. Проверка, что метод возвращает объект типа list
        collector.books_genre = {
            'Дюна': 'Фантастика'
        }
        result = collector.get_books_with_specific_genre('Фантастика')
        assert isinstance(result, list)

    def test_get_books_with_specific_genre_returns_only_books_of_requested_genre(collector):
    #9. Проверка, что в результат попадают только книги запрошенного жанра
        collector.books_genre = {
            'Дюна': 'Фантастика',
            'Основание': 'Фантастика',
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы'
        }
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Дюна', 'Основание']
