from flask import Flask, jsonify
from flask_restful import Api, Resource
from model.create_db import main
from model.db import select_query

app = Flask(__name__)
api = Api(app)


@app.before_first_request
def create_tables():
    main()

class Home(Resource):
    def get(self):
        return {"message": "Web API: Transactional Data Request"}, 200

class User(Resource):
    def get(self):
        return {'Correct Usage': 'URL + /user/User_CPF'}, 200

class UserTransaction(Resource):
    def get(self, cpf):
        query = f"SELECT * FROM tbl_user WHERE cpf = '{cpf}'"
        user = select_query(query)
        if user:
            user_id = user[0][0]
            query = f"SELECT * FROM tbl_bank WHERE usr_id = '{user_id}'"
            banks = select_query(query)
            if banks:
                banks_list = []
                transactions = []
                for bank in banks:
                    banks_list.append({
                        "bank_name": bank[2],
                        "bank_account": bank[3]
                    })
                    bank_id = bank[0]
                    query = f"SELECT * FROM tbl_transaction WHERE bank_id = '{bank_id}'"
                    transactions.append(select_query(query))
                context = {
                    "username": user[0][1],
                    "email": user[0][2],
                    "cpf": user[0][3],
                    "banks": banks_list,
                    "transactions": transactions
                }
                return context, 200
            return {'error': 'User not found'}, 404
        return {'error': 'User not found'}, 404


api.add_resource(Home, '/')

api.add_resource(User, '/user')

api.add_resource(UserTransaction, "/user/<string:cpf>")

if __name__ == "__main__":
    app.run(debug=False)
