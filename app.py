from flask import Flask, make_response, request, jsonify
from BrowsingAndSorting import BroswingAndSorting

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
    

# GET books by genre
@app.route('/books/genre/<genre>', methods=['GET'])
def books_by_genre(genre):
    if request.method == 'GET':
        sr = BroswingAndSorting()
        return jsonify(sr.list_by_genre(genre))
    return make_response('Method not allowed', 405)
    

# GET top ten selling books
@app.route('/books/best-sellers', methods=['GET'])
def best_sellers():
    if request.method == 'GET':
        sr = BroswingAndSorting()
        return jsonify(sr.list_best_sellers())
    return make_response('Method not allowed', 405)


# GET books by rating
@app.route('/books/rating/<rating:int>', methods=['GET'])
def books_by_rating(rating):
    if request.method == 'GET':
        sr = BroswingAndSorting()
        return jsonify(sr.list_by_rating(rating))
    return make_response('Method not allowed', 405)


# UPDATE to disount books by publisher
@app.route('/books/discount', methods=['POST'])
def discount_books():
    if request.method == 'POST':
        sr = BroswingAndSorting()
        publisher = request.json['publisher']
        discount = request.json['discount']
        return jsonify(sr.discount_by_publisher(publisher, discount))
    return make_response('Method not allowed', 405)
