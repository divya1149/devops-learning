from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask + MySQL App is Running! 🚀"

@app.route('/test-db')
def test_db():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'db'),
            user=os.environ.get('MYSQL_USER', 'root'),
            password=os.environ.get('MYSQL_PASSWORD', 'password'),
            database=os.environ.get('MYSQL_DATABASE', 'mydb')
        )
        return "Database Connected Successfully! ✅"
    except Exception as e:
        return f"Database Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
