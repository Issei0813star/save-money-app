from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import sqlite3
import json
import codecs

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
        target_month = request.args.get("targetMonth")

        conn = sqlite3.connect("../save-money-app.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM payment WHERE strftime('%Y-%m', date) = ?", (target_month,)
        )
        data = cursor.fetchall()

        conn.close()

        response_data = []

        for row in data:
            response_row = {
                "amount": row[0],
                "type": row[1],
                "category": row[2],
                "isCredit": row[3],
                "date": row[4],
            }
            response_data.append(response_row)

        response = {"data": response_data}
        response = app.response_class(
            response=json.dumps(response, ensure_ascii=False),
            status=200,
            mimetype="application/json",
        )
        return response


api.add_resource(Payment, "/api/payment")
api.add_resource(PaymentsMonth, "/api/payments/month")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
