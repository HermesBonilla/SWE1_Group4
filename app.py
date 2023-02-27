from flask import Flask, make_response, request, jsonify
from BookRepo import BookRepo

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# GET books by genre
@app.route('/books/genre/<genre>', methods=['GET'])
def books_by_genre(genre):
    if request.method == 'GET':
        sr = BookRepo()
        return jsonify(sr.list_by_genre(genre))
    return make_response('Method not allowed', 405)
    

# GET top ten selling books
@app.route('/books/best-sellers', methods=['GET'])
def best_sellers():
    if request.method == 'GET':
        sr = BookRepo()
        return jsonify(sr.list_best_sellers())
    return make_response('Method not allowed', 405)