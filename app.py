from flask import Flask, render_template, request, jsonify
from database_helper import DatabaseHelper

app = Flask(__name__)
app._static_folder = './static'
db_helper = DatabaseHelper('static/json/database.json')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/sales")
def sales():
    return render_template("sales.html")


@app.route("/query")
def query():
    rest_name = request.args.get("rn")
    food_type = request.args.get("ft")
    rand_seed = request.args.get("rs")
    rand_seed = float(rand_seed) if rand_seed else None
    query_result = db_helper.query(rest_name, meal_type, rand_seed)
    return jsonify(query_result)


if __name__ == '__main__':
    app.run()
