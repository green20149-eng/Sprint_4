class TestGetbooksForChildren:
# 1. Пустой словарь
    def test_empty_books_for_children(collector):
        assert collector.get_books_for_children() == []

# 2. Только детские жанры
    def test_only_children_genres(collector):
        collector.books_genre = {
            "Винни Пух": "Мультфильмы",
            "Комедия дня": "Комедии"
        }
        result = collector.get_books_for_children()
        assert set(result) == {"Винни Пух", "Комедия дня"}

# 3. Только возрастные жанры
    def test_only_age_restricted_genres(collector):
        collector.books_genre = {
            "Оно": "Ужасы",
            "Шерлок Холмс": "Детективы"
        }
        assert collector.get_books_for_children() == []

# 4. Смешанные жанры
    def test_mixed_genres(collector):
        collector.books_genre = {
            "Винни Пух": "Мультфильмы",
            "Оно": "Ужасы",
            "Дюна": "Фантастика",
            "Шерлок Холмс": "Детективы"
        }
        result = collector.get_books_for_children()
        assert set(result) == {"Винни Пух", "Дюна"}

# 5. Возвращается list
    def test_returns_list(collector):
        collector.books_genre = {"Книга": "Комедии"}
        assert isinstance(collector.get_books_for_children(), list)

# 6. Неизвестный жанр игнорируется
    def test_unknown_genre(collector):
        collector.books_genre = {"Книга": "Романтика"}
        assert collector.get_books_for_children() == []

# 7. Проверка включения допустимой книги
    def test_valid_book_included(collector):
        collector.books_genre = {
            "История игрушек": "Мультфильмы"
        }
        assert "История игрушек" in collector.get_books_for_children()

# 8. Проверка фильтрации age_rating
    def test_excludes_age_rating_only(collector):
        collector.books_genre = {
            "Фантастика книга": "Фантастика",
            "Ужасы книга": "Ужасы"
        }
        assert collector.get_books_for_children() == [
            "Фантастика книга"
        ]

# 9. Повторный вызов даёт тот же результат
    def test_consistency(collector):
        collector.books_genre = {
            "Винни Пух": "Мультфильмы",
            "Дюна": "Фантастика"
        }
        assert (
            collector.get_books_for_children() == collector.get_books_for_children()
        )
