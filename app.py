from flask import Flask, make_response, request, jsonify
from DatabaseSetup import Database

app = Flask(__name__)

@app.route('/')
def get_all_books():
    if request.method == 'GET':
        db = Database()
        return jsonify(db.get_all_books())