import json


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
            print(
                f"Wishlist with name '{name}' already exists for user {self.user_id}")
        else:
            self.wishlists[name] = Wishlist(name)
            print(
                f"Wishlist with name '{name}' created for user {self.user_id}")

    def list_wishlist_items(self, wishlist_names):
        wishlist_items = {}
        for wishlist_name in wishlist_names:
            if wishlist_name in self.wishlists:
                wishlist_items[wishlist_name] = self.wishlists[wishlist_name].items
            else:
                print(
                    f"Wishlist with name '{wishlist_name}' does not exist for user {self.user_id}")
        # indent = 2 for vertical format, separators =(',', ': ') for horizontal format
        return json.dumps(wishlist_items, indent=1, separators=(',', ': '))

    def remove_book_to_cart(self, wishlist_name, book_name):
        if wishlist_name in self.wishlists:
            if book_name in self.wishlists[wishlist_name].items:
                self.wishlists[wishlist_name].items.remove(book_name)
                self.shopping_cart.append(book_name)
                print(
                    f"Book '{book_name}' removed from wishlist '{wishlist_name}' and added to shopping cart")
            else:
                print(
                    f"Book '{book_name}' does not exist in wishlist '{wishlist_name}'")
        else:
            print(
                f"Wishlist with name '{wishlist_name}' does not exist for user {self.user_id}")


# create a user with ID 1
user1 = User(1)

# create a wishlist with name "retro" for user 1
user1.create_wishlist("Retro")

# create another wishlist with name "short" for user 1
user1.create_wishlist("Short")

book1 = "The Hitchhiker's Guide to the Galaxy"
user1.wishlists["Retro"].items.append(book1)

book2 = "1984"
user1.wishlists["Retro"].items.append(book2)

#book3 = "The Lord of the Rings"
book3 = {"name": "John", "age": 30, "city": "New York"}
user1.wishlists["Retro"].items.append(book3)

# list the items in the "Retro" and "Short" wishlists of user1 in JSON format
print(user1.list_wishlist_items(["Retro"]))

user1.remove_book_to_cart("Retro", "1984")
# print the contents of the shopping cart
print("CART: " + ", ".join(user1.shopping_cart))

print(user1.list_wishlist_items(["Retro"]))
