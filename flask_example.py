from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "Hello world"

@app.get("/add")
def add():
    return "1 + 1"

@app.route('/sum')
def calculate_sum():
    args = request.args

    if not args.get("n1"):
        return "n1 not set"

    if not args.get("n2"):
        return "n2 not set"

    n1 = float(args.get("n1"))
    n2 = float(args.get("n2"))
    total_sum = n1 + n2
    return str(total_sum)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
