from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a dictionary to store user's shopping cart
shopping_carts = {}

# Endpoint to add a book to the shopping cart
@app.route('/shopping_cart', methods=['POST'])
def add_book_to_cart():
    book_id = request.json['book_id']
    user_id = request.json['user_id']

    if user_id not in shopping_carts:
        shopping_carts[user_id] = []

    shopping_carts[user_id].append(book_id)

    return jsonify({'message': 'Book added to cart successfully'})

# Endpoint to retrieve the list of books in the shopping cart
@app.route('/shopping_cart', methods=['GET'])
def get_shopping_cart():
    user_id = request.args.get('user_id')

    if user_id not in shopping_carts:
        return jsonify([])

    return jsonify(books_in_cart)

# Endpoint to delete a book from the shopping cart
@app.route('/shopping_cart', methods=['DELETE'])
def delete_book_from_cart():
    book_id = request.args.get('book_id')
    user_id = request.args.get('user_id')

    if user_id not in shopping_carts:
        return jsonify({'message': 'Shopping cart is empty'})

    if book_id not in shopping_carts[user_id]:
        return jsonify({'message': 'Book is not in the cart'})

    shopping_carts[user_id].remove(book_id)

    return jsonify({'message': 'Book removed from cart successfully'})

# Endpoint to retrieve the subtotal of all items in the shopping cart
@app.route('/shopping_cart/subtotal', methods=['GET'])
def get_cart_subtotal():
    user_id = request.args.get('user_id')

    if user_id not in shopping_carts:
        return jsonify({'subtotal': 0})

    # Here you can retrieve the prices of books from your database or any other source
    books_prices = {'book_id_1': 10.99, 'book_id_2': 15.99, 'book_id_3': 20.99} # Example prices

    subtotal = sum([books_prices[book_id] for book_id in shopping_carts[user_id]])

    return jsonify({'subtotal': subtotal})

if __name__ == '__main__':
    app.run(debug=True)
