class TestSetBook:
# 1. Жанр успешно устанавливается для существующей книги
    def test_set_book_genre_success(collector):
        collector.books_genre['Дюна'] = ''
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.books_genre['Дюна'] == 'Фантастика'

# 2. Установка жанра "Ужасы"
    def test_set_book_genre_horror(collector):
        collector.books_genre['Оно'] = ''
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.books_genre['Оно'] == 'Ужасы'

# 3. Установка жанра "Детективы"
    def test_set_book_genre_detective(collector):
        collector.books_genre['Шерлок Холмс'] = ''
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.books_genre['Шерлок Холмс'] == 'Детективы'

# 4. Установка жанра "Мультфильмы"
    def test_set_book_genre_cartoons(collector):
        collector.books_genre['Король Лев'] = ''
        collector.set_book_genre('Король Лев', 'Мультфильмы')
        assert collector.books_genre['Король Лев'] == 'Мультфильмы'

# 5. Установка жанра "Комедии"
    def test_set_book_genre_comedy(collector):
        collector.books_genre['Маска'] = ''
        collector.set_book_genre('Маска', 'Комедии')
        assert collector.books_genre['Маска'] == 'Комедии'

# 6. Жанр не устанавливается для несуществующей книги
    def test_set_book_genre_book_not_exists(collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.books_genre

# 7. Жанр не устанавливается, если жанр отсутствует в списке допустимых
    def test_set_book_genre_invalid_genre(collector):
        collector.books_genre['Дюна'] = ''
        collector.set_book_genre('Дюна', 'Роман')
        assert collector.books_genre['Дюна'] == ''

# 8. Пустой жанр не устанавливается
    def test_set_book_genre_empty_genre(collector):
        collector.books_genre['Дюна'] = ''
        collector.set_book_genre('Дюна', '')
        assert collector.books_genre['Дюна'] == ''

# 9. Регистр имеет значение: жанр с неправильным регистром не устанавливается
    def test_set_book_genre_wrong_case(collector):
        collector.books_genre['Дюна'] = ''
        collector.set_book_genre('Дюна', 'фантастика')
        assert collector.books_genre['Дюна'] == ''
