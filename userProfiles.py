from flask import Flask, request
from app import get_app_name

app = get_app_name()


@app.route('/users', methods=['POST'])

def create_user():
    user = {
        'username': request.json.get('username', ''),
        'password': request.json.get('password', ''),
        'name': request.json.get('name', ''),
        'email': request.json.get('email', ''),
        'home_address': request.json.get('home_address', '')
    }
    users.append(user)
    return '', 201

if __name__ == '__main__':
    app.run()