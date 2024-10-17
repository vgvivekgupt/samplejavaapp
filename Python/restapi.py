from flask import Flask, jsonify, request

app = Flask(__name__)

#Dummy data for users
users = [

        {'id':1, 'name':'Vivek', 'age':26},
        {'id':2, 'name':'Tejvir', 'age':28},
        {'id':3, 'name':'Sameer', 'age':28}

        ]

#Get all users
@app.route('/user', methods=['GET'])
def get_users():
    return jsonify(users)

#Get a specific user by ID
@app.route('/users/<int:user_id>',
        methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if
user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404
#Post a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

#Put to update an existing user by ID
@app.route('/users/<int:user_id>',
methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if
user['id'] == user_id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user)
    return jsonify({'message': 'user not found'}), 404

#Delete a user by ID
@app.route('/users/<int:user_id>',
methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if
user['if'] != user_id]
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(host='192.168.242.111', port=9292, debug=True)
