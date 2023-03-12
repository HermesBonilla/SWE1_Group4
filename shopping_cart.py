from flask import Flask, make_response, request, jsonify
import requests
from app import get_app_name

app = get_app_name()


class ShoppingCart:
    def __init__(self, _user_id):
        self.book_list = []
        self.user_id = _user_id

    @app.route('/shopping_cart/<int:user_id>/add_book', methods=['POST'])
    def add_book_to_cart(self, book, user_id):
        self.book_list.append(book)
        return make_response(jsonify({"message": "Book added to shopping cart"}), 200)

    @app.route('/shopping_cart/<int:user_id>/remove_book', methods=['DELETE'])
    def remove_book_from_cart(self, book, user_id):  # user_id used in route
        self.book_list.remove(book)
        return make_response(jsonify({"message": "Book removed from shopping cart"}), 200)

    @app.route('/shopping_cart/<int:user_id>/get_books', methods=['GET'])
    def get_books_in_cart(self, user_id):
        return make_response(jsonify({self.book_list}), 200)

    @app.route('/shopping_cart/<int:user_id>/get_total_price', methods=['GET'])
    def get_total_price(self, user_id):
        total_price = 0
        for book in self.book_list:
            total_price += book.price  # assumes that book has a price attribute in class
        return make_response(jsonify({"total_price": total_price}), 200)
