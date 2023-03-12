from flask import Flask, make_response, request, jsonify
import requests
from app import get_app_name

app = get_app_name()


class BookDetails:
    def __init__(self, _book_id, _book_name, _book_author, _book_price, _book_date, book_genre, book_description, book_publisher):
        self.user_id = _book_id
        self.book_name = _book_name
        self.book_author = _book_author
        self.book_price = _book_price
        self.book_year = _book_date
        self.book_genre = book_genre
        self.book_description = book_description
        self.book_publisher = book_publisher

class BookAuthor:
    def __init__(self, _book_author_first_name, _book_author_last_name, book_author_bibliography, book_author_publisher):
        self.book_author_first_name = _book_author_first_name
        self.book_author_last_name = _book_author_last_name
        self.book_author_bibliography = book_author_bibliography
        self.book_author_publisher = book_author_publisher


    # Using book ID, retrieve book details from database
    @app.route('/book/<int:book_id>/get_details', methods=['GET'])
    def get_book_details(book_id):
        if book_id == 1:
            return jsonify({'book_id': book_id}, {'book_name': 'book_name'}, {'book_author': 'book_author'}, {'book_price': 'book_price'}, {'book_year': 'book_year'}, 
                       {'book_genre': 'book_genre'}, {'book_description': 'book_description'}, {'book_publisher': 'book_publisher'})
        else:
            return jsonify({'message': 'Book not found'}), 404
        

    # Using _book_author, retrieve books associated with author from database
    @app.route('/book/<string:book_author>/get_books_by_author', methods=['GET'])
    def get_books_by_author(book_author):
        if book_author == 1:
            return jsonify({'book_id': 'book_id'}, {'book_name': 'book_name'}, {'book_author': 'book_author'}, {'book_price': 'book_price'}, {'book_year': 'book_year'}, 
                       {'book_genre': 'book_genre'}, {'book_description': 'book_description'}, {'book_publisher': 'book_publisher'})
        else:
            return jsonify({'message': 'Author not found'}), 404
