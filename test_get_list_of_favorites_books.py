class TestGetList:
# 1. Проверка, что у нового экземпляра список избранных книг пустой
    def test_get_list_of_favorites_books_returns_empty_list_for_new_collector(collector):
        assert collector.get_list_of_favorites_books() == []

# 2. Проверка возврата списка с одной избранной книгой
    def test_get_list_of_favorites_books_returns_one_book(collector):
        collector.favorites.append('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']

# 3. # Проверка возврата списка с несколькими избранными книгами
    def test_get_list_of_favorites_books_returns_several_books(collector):
        collector.favorites.extend(['Дюна', 'Оно', 'Шерлок Холмс'])
        assert collector.get_list_of_favorites_books() == [
            'Дюна',
            'Оно',
            'Шерлок Холмс'
        ]

# 4. ПроверкаЮ что порядок книг в списке не изменяется
    def test_get_list_of_favorites_books_preserves_order_of_books(collector):
        collector.favorites.extend(['Книга 1', 'Книга 2', 'Книга 3'])
        assert collector.get_list_of_favorites_books() == [
            'Книга 1',
            'Книга 2',
            'Книга 3'
        ]

# 5. Проверка, что метод возвращает объект типа list
    def test_get_list_of_favorites_books_returns_list_type(collector):
        assert isinstance(collector.get_list_of_favorites_books(), list)

# 6. Проверка наличия книги в жанре фантастики в списке избранного
    def test_get_list_of_favorites_books_with_fantasy_book(collector):
        collector.favorites.append('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

# 7. Проверка наличия книги в жанре ужасов в списке избранного
    def test_get_list_of_favorites_books_with_horror_book(collector):
        collector.favorites.append('Оно')
        assert 'Оно' in collector.get_list_of_favorites_books()

# 8. Проверка, что длина возвращаемого списка соответствует количеству избранных книг
    def test_get_list_of_favorites_books_length_matches_number_of_books(collector):
        collector.favorites.extend(['Дюна', 'Оно'])
        assert len(collector.get_list_of_favorites_books()) == 2

# 9. Проверка, что метод возвращает именно атрибут favorites, а не его копию
    def test_get_list_of_favorites_books_returns_actual_favorites_list(collector):
        collector.favorites.append('Дюна')
        result = collector.get_list_of_favorites_books()
        assert result is collector.favorites
