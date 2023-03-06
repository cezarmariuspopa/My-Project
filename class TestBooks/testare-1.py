from requests_api.books import *

class TestBooks:

    def test_get_books_200(self):
        response = get_books()
        assert response.status_code == 200, 'Status code is not ok'

    def test_get_books_invalid_type(self):
        response = get_books(book_type='abc')
        # print(response.status_code)
        # print(response.json())
        assert response.status_code == 300, 'Status code is not ok'
        assert response.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: comedy, non-comedy."

    def test_get_all_books(self):
        response = get_books()
        assert len(response.json()) == 6, 'Books total is incorrect'

    def test_get_all_books_limit(self):
        response = get_books(limit=3)
        assert len(response.json()) == 6,"Total books returned is incorrect"

    def test_get_all_books_type_fiction(self):
        response = get_books(book_type='comedy')
        assert len(response.json()) == 4, "Total books returned is incorrect"

    def test_get_all_books_type_non_fiction(self):
        response = get_books(book_type='non-comedy')
        assert len(response.json()) == 2, "Total books returned is incorrect"
        for book in response.json():
            assert book['type'] == 'non-comedy'

    def test_get_all_books_type_and_limit(self):
        response = get_books(book_type='comedy',limit=2)
        assert len(response.json()) == 4,'Total books returned is incorrect'
        # for book in response.json():
        #     assert book['type'] == 'comedy', 'Book type returned is incorrect'

    def test_get_book(self):
        response = get_book(1)
        expected = {
            "id": 1,
            "name": "The Russian",
            "author": "James Patterson and James O. Born",
            "isbn": "1780899475",
            "type": "comedy",
            "price": 12.98,
            "current-stock": 12,
            "available": True
        }
        assert response.status_code == 200, 'Status code is not correct'
        assert response.json() == expected, 'Response body is not correct'

    def test_get_book_invalid_id(self):
        response = get_book(15)
        assert response.status_code == 404, 'Status code is not correct'
        assert response.json()['error'] == 'No book with id 15'