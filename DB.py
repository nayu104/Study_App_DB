import mysql.connector
from config import DB_CONFIGF

def conn_db():
    return mysql.connector.connect(**DB_CONFIGF)
    # `connect()` の引数は決まった書き方
    #Flask から MySQL に接続する関数を作成


    