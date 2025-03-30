from flask import Flask, jsonify
from DB import conn_db
import json 
from flask_cors import CORS
import os
from flask import Flask, request

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#@app.route("/") → /（ルート）にアクセスしたとき、この関数を実行する
@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/users",methods=["GET"])
def get_users():
    conn = conn_db()#DB接続
    cursor_db= conn.cursor(dictionary=True)#カーソル＝入力形式
    cursor_db.execute("SELECT * FROM users")#SQL文実行
    row = cursor_db.fetchall()#データ取得
    conn.close() 
    return jsonify(row)

#ユーザーアイコンのアップロード
ICON_FOLDER = "icons"
@app.route("/icons",methods=["POST"])
def post_Usericons():
    upLoadFile = request.files["icons"]
    original_fileName = upLoadFile.filename
    save_filePath = os.path.join(ICON_FOLDER,original_fileName)
    upLoadFile.save(save_filePath)
    return jsonify({"保存完了":original_fileName})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)#app.runはFlaskアプリケーションを起動するメソッド
#デバッグモードを有効にする


