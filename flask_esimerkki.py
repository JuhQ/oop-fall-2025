from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello"

@app.route("/user")
def tulosta_user():
    return ""

@app.route("/summa")
def summaa_luvut():
    args = request.args

    try:
        arvo1 = int(args.get("n1"))
        arvo2 = int(args.get("n2"))


        tulos = {
            "luku1": arvo1,
            "luku2": arvo2,
            "tulos": arvo1 + arvo2
        }

        return tulos
        #return f"{arvo1 + arvo2}"
        #return str(n1 + n2)
    except ValueError:
        response = {
            "message": "Virheellinen luku",
            "status_code": 400,
            "input": {"value1": args.get("n1"), "value2": args.get("n2")}
        }

        json_vastaus = json.dumps(response)
        return Response(
            response=json_vastaus,
            status=400,
            # kokeile I'm a teapot
            #status=418,
            mimetype="application/json"
        )


@app.route("/kaiku/<teksti>")
def kaiku(teksti):
    return {"kaiku": f"{teksti} {teksti}"}


@app.errorhandler(404)
def handle_error_404(error_code):
    return "oh no - 404"

@app.errorhandler(500)
def handle_error_500(error_code):
    return "oh no - 500"

app.run(host="127.0.0.1", port=3000, use_reloader=True)
