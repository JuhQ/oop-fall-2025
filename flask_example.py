from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "Hello world"

@app.get("/add")
def add():
    return "1 + 1"

@app.route('/sum/<n1>/<n2>')
def calculate_sum(n1, n2):
    args = request.args
    try:
        n1 = float(n1)
        n2 = float(n2)
        total_sum = n1 + n2

        json_data = {
            "number1": n1,
            "number2": n2,
            "total": total_sum
        }

        return json_data

    except ValueError:
        response = {
            "message": "Invalid number",
            "input": {"value1": n1, "value2": n2},
            "status": 400
        }

        json_response = json.dumps(response)
        http_response = Response(
            response=json_response,
            status=response["status"],
            mimetype="application/json"
        )
        return http_response


@app.get("/echo/<text>")
def echo(text):
    return {
        "echo_data": f"{text} {text}"
    }

@app.get("/user/<id>")
def get_user(id):
    # ... get user data from db with id
    return {
        "user_id": id,
        "name": "Juha"
    }

@app.errorhandler(404)
def handle_errors(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
