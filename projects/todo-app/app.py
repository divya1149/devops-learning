from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'db'),
        user=os.environ.get('MYSQL_USER', 'root'),
        password=os.environ.get('MYSQL_PASSWORD', 'password'),
        database=os.environ.get('MYSQL_DATABASE', 'tododb')
    )

@app.route('/')
def home():
    return "To-Do App is Running! 🚀"

@app.route('/todos', methods=['GET'])
def get_todos():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
        return jsonify(todos)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/todos', methods=['POST'])
def add_todo():
    try:
        data = request.json
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO todos (task) VALUES (%s)",
            (data['task'],)
        )
        conn.commit()
        return jsonify({"message": "Todo added successfully! ✅"})
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)