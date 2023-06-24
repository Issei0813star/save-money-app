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

        def get_over_all(target, value):
            total = sum(
                item["amount"] for item in response_data if item[target] == value
            )
            return total

        total_spending = get_over_all("type", "spending")
        total_income = get_over_all("type", "income")
        food_costs = get_over_all("category", "食費")
        daily_necessities_costs = get_over_all("category", "日用品")
        fashion_costs = get_over_all("category", "ファッション")
        entertainment_costs = get_over_all("category", "交際費")
        vape_costs = get_over_all("category", "Vape")
        utility_costs = get_over_all("category", "光熱費")
        housing_costs = get_over_all("category", "住居費")
        work_tools_costs = get_over_all("category", "食費")
        transportation_costs = get_over_all("category", "食費")

        response = {
            "total_payments": total_spending,
            "total_income": total_income,
            "category_defs_costs": {
                "food": food_costs,
                "daily_necessities": daily_necessities_costs,
                "fashion": fashion_costs,
                "entertainment": entertainment_costs,
                "vape": vape_costs,
                "utility": utility_costs,
                "housing": housing_costs,
                "work_tools": work_tools_costs,
                "transportation": transportation_costs,
            },
        }
        return response


api.add_resource(Payment, "/api/payment")
api.add_resource(PaymentsMonth, "/api/payments/month")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
