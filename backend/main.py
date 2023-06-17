from flask import Flask, render_template, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import sqlite3

app = Flask(
    __name__,
    static_folder="../frontend/dist/static",
    template_folder="../frontend/dist",
)
CORS(app)
api = Api(app)


class Payment(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("amount", type=int, required=True)
        parser.add_argument("type", type=str, required=True)
        parser.add_argument("category", type=str, required=True)
        parser.add_argument("isCredit", type=int, required=True)
        parser.add_argument("date", type=str, required=True)
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


class PaymentsMonth(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("targetMonth", type=str, required=True)
        args = parser.parse_args()

        conn = sqlite3.connect("../save-money-app.db")
        cursor = conn.cursor()

        target_month = args["targetMonth"]

        cursor.execute(
            "SELECT * FROM payment WHERE strftime('%Y-%m', date) = ?", (target_month,)
        )
        data = cursor.fetchall()

        conn.close()

        response = {"data": data}
        return response


api.add_resource(Payment, "/api/payment")
api.add_resource(PaymentsMonth, "/api/payments/month")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
