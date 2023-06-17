from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse
import sqlite3

app = Flask(
    __name__,
    static_folder="../frontend/dist/static",
    template_folder="../frontend/dist",
)
api = Api(app)
# リクエストパーサーを作成
parser = reqparse.RequestParser()
parser.add_argument("amount", type=int, required=True)
parser.add_argument("type", type=str, required=True)
parser.add_argument("category", type=str, required=True)
parser.add_argument("isCredit", type=int, required=True)
parser.add_argument("date", type=str, required=True)


class Payment(Resource):
    def post(self):
        args = parser.parse_args()

        conn = sqlite3.connect("../save-money-app.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO payment (amount, type, category, isCredit, date) VALUES (?, ?, ?, ?, ?)",
            (
                args["amount"],
                args["type"],
                args["category"],
                args["isCredit"],
                args["date"],
            ),
        )

        conn.commit()

        conn.close()
        return {"message": "データが正常に保存されました。"}, 200


api.add_resource(Payment, "/api/payment")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
