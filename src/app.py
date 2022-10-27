from flask import Flask, jsonify
from flask_restful import Api, Resource
from model.create_db import main
from model.db import select_query

app = Flask(__name__)
api = Api(app)


@app.before_first_request
def create_tables():
    main()


class UserTransaction(Resource):
    def get(self, cpf):
        query = f"SELECT * FROM tbl_user WHERE cpf = '{cpf}'"
        user = select_query(query)
        if user:
            user_id = user[0][0]
            query = f"SELECT * FROM tbl_bank WHERE usr_id = '{user_id}'"
            bank = select_query(query)
            if bank:
                bank_id = bank[0][0]
                query = f"SELECT * FROM tbl_transaction WHERE bank_id = '{bank_id}'"
                transactions = select_query(query)
                return jsonify(transactions), 200
            return jsonify({'error': 'User not found'}), 404


api.add_resource(UserTransaction, "/user/<string:cpf>")

if __name__ == "__main__":
    app.run(debug=True)
