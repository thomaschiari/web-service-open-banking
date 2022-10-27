from re import I
from flask import Flask
from flask_restful import Api, Resource
from model.create_db import create_db, load_table_user, load_table_bank, load_table_transaction
from pathlib import Path


app = Flask(__name__)
api = Api(app)

@app.before_first_request
def create_tables():
    path_db = Path(__file__).parent / 'db.sqlite3'
    path_csv = Path(__file__).parent / 'csv_users.csv'
    create_db(path_db)
    load_table_user(path_db, path_csv)
    path_csv = Path(__file__).parent / 'table_bankinfo.csv'
    load_table_bank(path_db, path_csv)
    path_csv = Path(__file__).parent / 'table_transactions.csv'
    load_table_transaction(path_db, path_csv)

class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

class OpenBanking(Resource):
    def get(self):
        return {"data": "Open Banking"}

api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)
