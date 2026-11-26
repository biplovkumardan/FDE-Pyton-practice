from flask import Flask, request, jsonify
# Install them in your project’s active environment
# python -m pip install Flask-Cors mysql-connector-python
from flask_cors import CORS
import mysql.connector

app =Flask(__name__)
CORS(app)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'dev'
}

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(**db_config)
"""
EXPLAINATION
---------------------------------------
In mysql.connector.connect(**db_config), ** unpacks a dictionary into keyword arguments.

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "company_db"
}

This call:
    mysql.connector.connect(**db_config)

is equivalent to:

mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dev"
)

The dictionary keys need to match valid argument names for connect().

"""

# 1 Get all users
@app.route('/users', methods =['GET'])
def get_users():
    conn = get_db_connection()
    cursor =conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)
"""
EXPLAINATION
---------------------------------------
The dictionary=True option makes query results come back as dictionaries keyed by column name, rather than tuples.
    cursor.execute("SELECT id, name, email FROM dev.users")
    user = cursor.fetchone()
    # Example: {'id': 1, 'name': 'Aarav Sharma', 'email': 'aarav.sharma@example.com'}

    Without dictionary=True, the row would typically be a tuple, 
        such as (1, 'Aarav Sharma', 'aarav.sharma@example.com').

"""

# 2 Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s",(user_id,))
    user =cursor.fetchone()
    cursor.close()
    conn.close()
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

# 3 Add a new user
@app.route('/users/add', methods=['POST'])
def add_user():
    data =request.json
    name = data.get('name')
    email = data.get('email')
    if not name:
        return jsonify({'error':'Name is required'})
    if not email:
        return jsonify({'error':'Email is required'})

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        return jsonify({'message':'User added successfully'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)})
    finally:
        cursor.close()
        conn.close()

# 4 Update user by ID
@app.route('/users/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if not name:
            return jsonify({'error':'Name is required'})
    if not email:
            return jsonify({'error':'Email is required'})

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s",(user_id,))
    if not cursor.fetchone():
         return jsonify({'error':'User not found'}), 404

    try:
         cursor.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s",
            (name, email, user_id)  
         )
         conn.commit()
         return jsonify({'message':'User updated successfully'})
    except mysql.connector.Error as err:
         return jsonify({'error':str(err)}), 500
    finally:
         cursor.close()
         conn.close()

# 5 Delete user by ID
@app.route('/users/delete/<int:user_id>', methods =['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    if not cursor.fetchone():
        return jsonify({'error': 'User not found'}), 404

    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        return jsonify({'message': 'User deleted successfully'})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        conn.close()
     
# Simple Hello route
@app.route('/')
def index():
    return "Hello"

# Entry Point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)