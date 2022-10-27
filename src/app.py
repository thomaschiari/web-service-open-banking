from re import I
from flask import Flask
from flask_restful import Api, Resource
from model.create_db import main
from pathlib import Path
from model.db import select_query


app = Flask(__name__)
api = Api(app)

@app.before_first_request
def create_tables():
    main()

class UserTransaction(Resource):
    def get(self, cpf):
        return {"data": "Transaction"}

api.add_resource(UserTransaction, "/user/<string:cpf>")

if __name__ == "__main__":
    app.run(debug=True)
