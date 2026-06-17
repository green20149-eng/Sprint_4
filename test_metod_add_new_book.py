class TestAddNewBook:
    # 1. Успешное добавление книги с валидным названием
    def test_add_new_book_adds_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre
        assert collector.books_genre['Гарри Поттер'] == ''

    # 2. Добавление книги длиной 1 символ
    def test_add_new_book_with_min_length_name(self, collector):
        collector.add_new_book('A')
        assert 'A' in collector.books_genre

    # 3. Добавление книги длиной 40 символов
    def test_add_new_book_with_max_allowed_length(self, collector):
        name = 'А' * 40
        collector.add_new_book(name)
        assert name in collector.books_genre

    # 4. Книга с пустым названием не добавляется
    def test_add_new_book_with_empty_name_not_added(self, collector):
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    # 5. Книга длиной 41 символ не добавляется
    def test_add_new_book_with_length_41_not_added(self, collector):
        name = 'А' * 41
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # 6. Книга длиной больше 41 символа не добавляется
    def test_add_new_book_with_too_long_name_not_added(self, collector):
        name = 'А' * 50
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # 7. Повторное добавление той же книги не создает дубликат
    def test_add_new_book_duplicate_not_added_twice(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.books_genre) == 1

    # 8. После повторного добавления значение жанра не меняется
    def test_add_new_book_duplicate_keeps_existing_genre(self, collector):
        collector.add_new_book('Дюна')
        collector.books_genre['Дюна'] = 'Фантастика'
        collector.add_new_book('Дюна')
        assert collector.books_genre['Дюна'] == 'Фантастика'

    # 9. Можно добавить несколько разных книг
    def test_add_new_book_adds_several_different_books(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        assert len(collector.books_genre) == 3
