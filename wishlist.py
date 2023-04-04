import json
from flask import Flask, request

app = Flask(__name__)

class Wishlist:
    def __init__(self, name):
        self.name = name
        self.items = []


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.wishlists = {}
        self.shopping_cart = []  # testing: create an empty shopping cart for the user

    def create_wishlist(self, name):
        if name in self.wishlists:
            return {"message": f"Wishlist with name '{name}' already exists for user {self.user_id}"}
        else:
            self.wishlists[name] = Wishlist(name)
            return {"message": f"Wishlist with name '{name}' created for user {self.user_id}"}

    def list_wishlist_items(self, wishlist_name):
        if wishlist_name in self.wishlists:
            return {"wishlist_name": wishlist_name, "items": self.wishlists[wishlist_name].items}
        else:
            return {"message": f"Wishlist with name '{wishlist_name}' does not exist for user {self.user_id}"}

    def add_book_to_wishlist(self, wishlist_name, book_id):
        if wishlist_name in self.wishlists:
            if book_id in self.wishlists[wishlist_name].items:
                return {"message": f"Book with ID '{book_id}' already exists in wishlist '{wishlist_name}'"}
            else:
                self.wishlists[wishlist_name].items.append(book_id)
                return {"message": f"Book with ID '{book_id}' added to wishlist '{wishlist_name}'"}
        else:
            return {"message": f"Wishlist with name '{wishlist_name}' does not exist for user {self.user_id}"}

    def remove_book_from_wishlist(self, wishlist_name, book_id):
        if wishlist_name in self.wishlists:
            if book_id in self.wishlists[wishlist_name].items:
                self.wishlists[wishlist_name].items.remove(book_id)
                return {"message": f"Book with ID '{book_id}' removed from wishlist '{wishlist_name}'"}
            else:
                return {"message": f"Book with ID '{book_id}' does not exist in wishlist '{wishlist_name}'"}
        else:
            return {"message": f"Wishlist with name '{wishlist_name}' does not exist for user {self.user_id}"}

@app.route("/users/<int:user_id>/wishlists", methods=["POST"])
def create_wishlist(user_id):
    wishlist_name = request.json.get("wishlist_name")
    user = User(user_id)
    return json.dumps(user.create_wishlist(wishlist_name))

@app.route("/wishlists/<string:wishlist_name>/items", methods=["GET"])
def list_wishlist_items(wishlist_name):
    user_id = request.args.get("user_id")
    user = User(user_id)
    return json.dumps(user.list_wishlist_items(wishlist_name))

@app.route("/wishlists/<string:wishlist_name>/items", methods=["POST"])
def add_book_to_wishlist(wishlist_name):
    user_id = request.args.get("user_id")
    user = User(user_id)
    book_id = request.json.get("book_id")
    return json.dumps(user.add_book_to_wishlist(wishlist_name, book_id))

@app.route("/wishlists/<string:wishlist_name>/items/<string:book_id>", methods=["DELETE"])
def remove_book_from_wishlist(wishlist_name, book_id):
    user_id = request.args.get("user_id")
    user = User(user_id)
    return json.dumps(user.remove_book_from_wishlist(wishlist_name, book_id))

if __name__ == "__main__":
    app
    