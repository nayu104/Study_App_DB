from flask import Flask, jsonify
from DB import conn_db

app = Flask(__name__)

#@app.route("/") → /（ルート）にアクセスしたとき、この関数を実行する
@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/users",methods=["GET"])
def get_users():
    conn = conn_db()
    cursor_db= conn.cursor(dictionary=True)
    cursor_db.execute("SELECT * FROM users")
    row = cursor_db.fetchall()
    conn.close()
    
    return jsonify(row)
