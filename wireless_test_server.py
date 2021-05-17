from flask import Flask
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
api = Api(app)

request = reqparse.RequestParser()


class CentralController(Resource):
    @staticmethod
    def get():
        return "You can use post to post new data to the server"

    @staticmethod
    def post():
        request.add_argument("data")
        args = request.parse_args()
        return {"data-wireless": args["data"]} if "data" in args else {"error-wireless": "Nothing received"}


api.add_resource(CentralController, '/post-data')

if __name__ == "__main__":
    app.run(debug=False, host="node-01.central.peppsaf", port=5253)
