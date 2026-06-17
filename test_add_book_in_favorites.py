class TestAddBook:
# 1. Книга добавляется в избранное, если есть в books_genre
    def test_add_existing_book_to_favorites(collector):
        collector.books_genre = {"Дюна": "Фантастика"}
        collector.add_book_in_favorites("Дюна")
        assert "Дюна" in collector.favorites

# 2. Книга НЕ добавляется, если её нет в books_genre
    def test_add_non_existing_book_not_added(collector):
        collector.books_genre = {"Дюна": "Фантастика"}
        collector.add_book_in_favorites("Оно")
        assert "Оно" not in collector.favorites

# 3. Повторное добавление не дублирует книгу
    def test_add_book_no_duplicates(collector):
        collector.books_genre = {"Дюна": "Фантастика"}
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Дюна")
        assert collector.favorites == ["Дюна"]

# 4. Добавление нескольких разных книг
    def test_add_multiple_books(collector):
        collector.books_genre = {
            "Дюна": "Фантастика",
            "Винни Пух": "Мультфильмы"
        }
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Винни Пух")
        assert set(collector.favorites) == {"Дюна", "Винни Пух"}

# 5. favorites остаётся пустым, если ничего не добавляли
    def test_favorites_empty_initially(collector):
        assert collector.favorites == []


# 6. Метод возвращает None (побочный эффект)
    def test_method_returns_none(collector):
        collector.books_genre = {"Дюна": "Фантастика"}
        result = collector.add_book_in_favorites("Дюна")
        assert result is None

# 7. Добавление книги не влияет на books_genre
    def test_books_genre_not_changed(collector):
        collector.books_genre = {"Дюна": "Фантастика"}
        collector.add_book_in_favorites("Дюна")
        assert collector.books_genre == {"Дюна": "Фантастика"}

# 8. Проверка длины списка favorites
    def test_favorites_length_increases(collector):
        collector.books_genre = {
            "Дюна": "Фантастика",
            "Винни Пух": "Мультфильмы"
        }
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Винни Пух")
        assert len(collector.favorites) == 2

# 9. Проверка добавления одной книги не влияет на другую
    def test_one_book_addition_isolated(collector):
        collector.books_genre = {
            "Дюна": "Фантастика",
            "Оно": "Ужасы"
       }
        collector.add_book_in_favorites("Дюна")
        assert collector.favorites == ["Дюна"]
        assert "Оно" not in collector.favorites
