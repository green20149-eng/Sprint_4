class TestDeleteBook:

    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)
# 1. Удаление книги из favorites
    def test_delete_existing_book(collector):
        collector.favorites = ["Дюна"]
        collector.delete_book_from_favorites("Дюна")
        assert "Дюна" not in collector.favorites

# 2. Удаление книги, которой нет в favorites
    def test_delete_non_existing_book(collector):
        collector.favorites = ["Дюна"]
        collector.delete_book_from_favorites("Оно")
        assert collector.favorites == ["Дюна"]

# 3. Удаление из пустого списка
    def test_delete_from_empty_favorites(collector):
        collector.favorites = []
        collector.delete_book_from_favorites("Дюна")
        assert collector.favorites == []

# 4. Удаление одного элемента из нескольких
    def test_delete_one_of_many(collector):
        collector.favorites = ["Дюна", "Оно", "Винни Пух"]
        collector.delete_book_from_favorites("Оно")
        assert collector.favorites == ["Дюна", "Винни Пух"]

# 5. Проверка, что метод возвращает None
    def test_method_returns_none(collector):
        collector.favorites = ["Дюна"]
        result = collector.delete_book_from_favorites("Дюна")
        assert result is None


# 6. Список изменяется только при наличии книги
    def test_list_changes_only_if_book_exists(collector):
        collector.favorites = ["Дюна"]
        collector.delete_book_from_favorites("Дюна")
        assert collector.favorites == []

# 7. Удаление не влияет на books_genre
    def test_books_genre_not_changed(collector):
        collector.books_genre = {"Дюна": "Фантастика"}
        collector.favorites = ["Дюна"]
        collector.delete_book_from_favorites("Дюна")
        assert collector.books_genre == {"Дюна": "Фантастика"}

# 8. Проверка длины списка после удаления
    def test_favorites_length_decreases(collector):
        collector.favorites = ["Дюна", "Оно"]
        collector.delete_book_from_favorites("Дюна")
        assert len(collector.favorites) == 1

# 9. Повторное удаление не вызывает ошибок
    def test_repeated_delete_does_not_fail(collector):
        collector.favorites = ["Дюна"]
        collector.delete_book_from_favorites("Дюна")
        collector.delete_book_from_favorites("Дюна")
        assert collector.favorites == []
